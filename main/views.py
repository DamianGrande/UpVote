from django.shortcuts import render

from main.models import Submission


def home_view(request):
    if not Submission.objects.count():
        Submission.objects.create(title=r"L&#39;ora è giunta.", description='Tutti questi anni per cosa?', votes=21,
                                  avatar="../static/images.png", submission_image='../static/images.png')
    return render(request, 'main/home_view.html', {'submission': Submission.objects.first()})
