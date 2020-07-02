from unittest.mock import patch

from .abstract_extractor_test import ExtractorTest
from DownloaderForReddit.extractors.direct_extractor import DirectExtractor
from Tests.mockobjects.MockObjects import get_post


@patch(f'DownloaderForReddit.extractors.base_extractor.BaseExtractor.make_dir_path')
@patch(f'DownloaderForReddit.extractors.base_extractor.BaseExtractor.make_title')
@patch(f'DownloaderForReddit.extractors.base_extractor.BaseExtractor.check_duplicate_content')
class TestDirectExtractor(ExtractorTest):

    def test_extract_direct_link(self, check_duplicate, make_title, make_dir_path):
        url = 'https://unsupported_site.com/image/3jfd9nlksd.jpg'
        post = get_post(url=url)
        self.session.add(post)

        check_duplicate.return_value = True
        make_title.return_value = post.title
        make_dir_path.return_value = 'content_dir_path'

        de = DirectExtractor(post)
        de.extract_content()

        self.check_output(de, url, post)
