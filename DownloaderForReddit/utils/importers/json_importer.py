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

import json
import logging
from datetime import datetime

from DownloaderForReddit.database.models import User, Subreddit
from DownloaderForReddit.database.model_enums import (LimitOperator, PostSortMethod, NsfwFilter, CommentDownload,
                                                      CommentSortMethod)

logger = logging.getLogger(__name__)


EXPELLED_KEYS = ['lists', 'posts', 'content', 'comments']
TYPE_MAP = {
    'date_created': lambda x: datetime.strptime(x, '%m/%d/%Y %I:%M %p'),
    'post_score_limit_operator': lambda x: LimitOperator(x),
    'post_sort_method': lambda x: PostSortMethod(x),
    'download_nsfw': lambda x: NsfwFilter(x),
    'extract_comments': lambda x: CommentDownload(x),
    'download_comments': lambda x: CommentDownload(x),
    'download_comment_content': lambda x: CommentDownload(x),
    'comment_score_limit_operator': lambda x: LimitOperator(x),
    'comment_sort_method': lambda x: CommentSortMethod(x),
    'date_added': lambda x: datetime.strptime(x, '%m/%d/%Y %I:%M %p'),
    'absolute_date_limit': lambda x: datetime.strptime(x, '%m/%d/%Y %I:%M %p'),
    'date_limit': lambda x: datetime.strptime(x, '%m/%d/%Y %I:%M %p')
}


def import_json(file_path):
    reddit_objects = []
    with open(file_path, 'r', encoding='utf-8') as file:
        j = json.load(file)
        try:
            reddit_object_data = _get_reddit_objects(j)
            objects_imported = 0
            for ro_element in reddit_object_data:
                model = User if ro_element['object_type'] == 'USER' else Subreddit
                _clean_ro_element(ro_element)
                reddit_object = model(**ro_element)
                objects_imported += 1
                reddit_objects.append(reddit_object)
            logger.info('Imported reddit objects from json file', extra={'file_path': file_path,
                                                                         'import_count': objects_imported})
        except KeyError:
            pass
    return reddit_objects


def _get_reddit_objects(json_element):
    try:
        ros = json_element['reddit_objects']
    except KeyError:
        ros = []
        for ro_list in json_element['reddit_object_lists']:
            ros.extend(ro_list['reddit_objects'])
    return ros


def _clean_ro_element(ro_element):
    for key in EXPELLED_KEYS:
        del ro_element[key]
    for key, value in ro_element.items():
        try:
            ro_element[key] = TYPE_MAP[key](value)
        except (KeyError, TypeError):
            pass
