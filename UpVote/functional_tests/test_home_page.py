import time
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

    def test_submissions_ordered_by_vote(self):
        self.browser.get(self.live_server_url)
        submissions = self.browser.find_elements_by_class_name('section')

        self.assertEqual('postCell 3', submissions[0].get_attribute('id'))
        self.assertEqual('postCell 1', submissions[1].get_attribute('id'))
        self.assertEqual('postCell 4', submissions[2].get_attribute('id'))
        self.assertEqual('postCell 2', submissions[3].get_attribute('id'))

    def test_update_votes(self):
        self.browser.get(self.live_server_url)

        vote_div = self.browser.find_element_by_id('votes 1')
        span = vote_div.find_element_by_tag_name('span')
        up_vote_icon = span.find_element_by_tag_name('i')
        current_vote = int(span.find_element_by_class_name('has-text-info').text)
        up_vote_icon.click()

        self.assertEqual(current_vote + 1, int(span.find_element_by_class_name('has-text-info').text))

    def test_border_for_high_number_of_votes(self):
        self.browser.get(self.live_server_url)

        post_cell_1 = self.browser.find_element_by_id('postCell 1')
        post_cell_2 = self.browser.find_element_by_id('postCell 2')

        self.assertEqual(0, len(post_cell_2.find_elements_by_class_name('blue-border')))
        self.assertEqual(1, len(post_cell_1.find_elements_by_class_name('blue-border')))

    if __name__ == '__main__':
        unittest.main()
