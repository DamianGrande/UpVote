from django.test import TestCase

from main.models import Submission


class TestHomeView(TestCase):

    def test_home_view_uses_correct_template(self):
        self.assertTemplateUsed(self.client.get(r'/'), 'main/home_view.html')

    def test_home_view_create_submissions(self):
        self.assertEqual(0, Submission.objects.count())

        self.client.get(r'/')

        self.assertEqual(4, Submission.objects.count())

        self.client.get(r'/')

        self.assertEqual(4, Submission.objects.count())
