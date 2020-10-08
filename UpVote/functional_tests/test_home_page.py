import unittest

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class HomePageTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def test_correct_title_on_heading(self):
        self.browser.get(self.live_server_url)

        self.assertEqual('UpVote!', self.browser.find_element_by_tag_name('h2').text)

    def test_correct_title_on_title_tag(self):
        self.browser.get(self.live_server_url)

        self.assertEqual('UpVote!', self.browser.title)

    def test_submission_structure(self):
        self.browser.get(self.live_server_url)

        post_cell = self.browser.find_element_by_id(f'postCell {1}')
        post_cell.find_element_by_id(f'image {1}')
        self.browser.find_element_by_id(f'votes {1}')
        post_content = post_cell.find_element_by_id(f'postContent {1}')
        post_content.find_element_by_id(f'title {1}')
        post_content.find_element_by_id(f'message {1}')
        post_content.find_element_by_id(f'author {1}')

    def test_all_submissions_visible(self):
        self.browser.get(self.live_server_url)

        self.browser.find_element_by_id(f'postCell {1}')
        self.browser.find_element_by_id(f'postCell {2}')
        self.browser.find_element_by_id(f'postCell {3}')
        self.browser.find_element_by_id(f'postCell {4}')

    if __name__ == '__main__':
        unittest.main()
