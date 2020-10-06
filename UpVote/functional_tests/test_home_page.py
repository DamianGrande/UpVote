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

    def test_vote_post(self):
        self.browser.get(self.live_server_url)

        post_cell = self.browser.find_element_by_id('postCell')
        post_cell.find_element_by_tag_name('img')
        self.browser.find_element_by_id('votes')
        post_content = post_cell.find_element_by_id('postContent')
        post_content.find_element_by_id('title')
        post_content.find_element_by_id('message')
        post_content.find_element_by_id('author')

    if __name__ == '__main__':
        unittest.main()
