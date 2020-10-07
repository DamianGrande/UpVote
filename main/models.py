from django.db import models


class Submission(models.Model):
    title = models.TextField(default='')
    description = models.TextField(default='')
    url = models.TextField(default='')
    votes = models.IntegerField(default=0)
    avatar = models.TextField(default='')
    submission_image = models.TextField(default='')
