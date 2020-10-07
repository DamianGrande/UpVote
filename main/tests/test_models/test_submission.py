from unittest import TestCase

from main.models import Submission


class TestSubmission(TestCase):

    def test_submission_saved_and_retrieved_correctly(self):
        self.assertEqual(0, Submission.objects.count())

        title = 'Submission title.'
        description = 'Submission description.'
        url = 'https://localhost/'
        votes = 34
        avatar = '../static/images.png'
        submission_image = '../static/images.png'
        Submission.objects.create(title=title, description=description, url=url, votes=votes, avatar=avatar,
                                  submission_image=submission_image)

        self.assertEqual(1, Submission.objects.count())

        submission = Submission.objects.first()

        self.assertEqual(title, submission.title)
        self.assertEqual(description, submission.description)
        self.assertEqual(url, submission.url)
        self.assertEqual(votes, submission.votes)
        self.assertEqual(avatar, submission.avatar)
        self.assertEqual(submission_image, submission.submission_image)





