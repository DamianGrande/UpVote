from django.test import TestCase


class TestHomeView(TestCase):

    def test_home_view_uses_correct_template(self):
        self.assertTemplateUsed(self.client.get(r'/'), 'main/home_view.html')
