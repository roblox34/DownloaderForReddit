"""
Downloader for Reddit takes a list of reddit users and subreddits and downloads content posted to reddit either by the
users or on the subreddits.


Copyright (C) 2017, Kyle Hickey


This file is part of the Downloader for Reddit.

Downloader for Reddit is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Downloader for Reddit is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Downloader for Reddit.  If not, see <http://www.gnu.org/licenses/>.
"""

import logging
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from time import time

from ..Utils import Injector

import requests

logger = logging.getLogger(__name__)
imgur_client = None
connection_attempts = 0
credit_time_limit = 1

_FREE_ENDPOINT = 'https://api.imgur.com/3/'
_RAPID_API_ENDPOINT = 'https://imgur-apiv3.p.rapidapi.com/3/'

credit_reset_time = 0
num_credits = 0


class ImgurError(Exception):

    def __init__(self, status_code):
        self.status_code = status_code


def _send_request(url_extension, retries = 1):
    if retries < 0:
        return
    headers = {
        'Authorization': 'Client-ID {}'.format(Injector.settings_manager.imgur_client_id)
    }
    if time() > credit_reset_time:
        check_credits()
    if num_credits > 0:
        url = _FREE_ENDPOINT + url_extension
    elif Injector.settings_manager.imgur_mashape_key is not None:
        url = _RAPID_API_ENDPOINT + url_extension
        headers['X-Mashape-Key'] = Injector.settings_manager.imgur_mashape_key
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    if response.status_code == 429:
        # Rate limiting.
        check_credits()
        _send_request(url_extension, retries - 1)
    raise ImgurError(response.status_code)


def check_credits():
    global num_credits, credit_reset_time
    url = _FREE_ENDPOINT + "credits"
    headers = {
        'Authorization': 'Client-ID {}'.format(Injector.settings_manager.imgur_client_id)
    }
    response = requests.get(url, headers=headers)
    result = response.json()
    credits_data = result['data']
    num_credits = min(credits_data['UserRemaining'], credits_data['ClientRemaining'])
    credit_reset_time = credits_data['UserReset']
    return num_credits


def get_album_images(album_id):
    json = _send_request('album/{}/images'.format(album_id))
    data = json['data']
    urls = [x['link'] for x in data]
    return urls

def get_client():
    """
    Configures and returns the imgur_client for application use.  If an error is encountered, connection will be
    attempted 3 times, then the exception is re-raised be passed on to be handled by the calling method.
    :return: The imgur client for the various parts of the application to use in interacting with imgur.
    :rtype: ImgurClient
    """
    global imgur_client
    global connection_attempts

    if not imgur_client:
        while connection_attempts < 3:
            try:
                client_id = Injector.settings_manager.imgur_client_id
                client_secret = Injector.settings_manager.imgur_client_secret
                mashape_key = Injector.settings_manager.imgur_mashape_key
                imgur_client = ImgurClient(client_id,client_secret)
                user_credits = imgur_client.credits['UserRemaining']
                if user_credits is not None and int(user_credits) <= 0:
                    if len(mashape_key) > 0:
                        imgur_client = ImgurClient(client_id, client_secret, mashape_key=mashape_key)
                connection_attempts = 0
                break
            except ImgurClientError as e:
                if e.status_code == 403 and e.error_message.startswith('Invalid client'):
                    handle_invalid_client()
                return None
            except Exception as e:
                if connection_attempts < 2:
                    connection_attempts += 1
                else:
                    raise e
    return imgur_client


def get_new_client():
    """
    Resets the imgur client then calls get_client to create a new instance.  A new instance is sometimes needed as
    once a client is established, the credit count does not refresh properly.
    :return: A new instance of an imgur_client
    :rtype: ImgurClient
    """
    global imgur_client
    imgur_client = None
    return get_client()


def handle_invalid_client():
    message = 'No valid Imgur client detected.  In order to download content from imgur.com, you must ' \
              'have a valid imgur client id and client secret.  Please see the imgur client information' \
              'dialog in the settings menu.'
    Injector.get_queue().put(message)
    logger.warning('Invalid imgur client id or secret')


def check_credit_time_limit():
    """
    Checks the global credit time limit (which is the time that the user imgur credits refresh) and returns True if the
    current time is greater than the limit (indicating there are credits remaining) and False if the time is less than
    the limit.
    :return: True if credits remain and False if not
    :rtype: bool
    """
    global credit_time_limit
    return time() > credit_time_limit


def set_credit_time_limit(refresh_time=(time() + 3605)):
    """
    Sets the global credit time limit to indicate when imgur user credits will refresh.  Defaults to one hour in the
    future from the current time.  The refresh limit can be supplied.
    :param refresh_time: The time at which the imgur user credits will refresh.
    :type refresh_time: int
    """
    global credit_time_limit
    credit_time_limit = refresh_time
