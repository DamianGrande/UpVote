
from django.shortcuts import render

from main.models import Submission


def home_view(request):
    Submission.objects.all().delete()
    if not Submission.objects.count():
        Submission.objects.create(id=1, title="Tempo scaduto.", description='Tutti questi anni per cosa?', votes=21,
                                  avatar="../static/images.png", submission_image='../static/images.png')
        Submission.objects.create(id=2, title="Punto di partenza.", description='Gli anni passano, ma nulla cambia.',
                                  votes=1,
                                  avatar="../static/images.png", submission_image='../static/images.png')
        Submission.objects.create(id=3, title="Tabula rasa.", description='Un altro ponte distrutto.', votes=34,
                                  avatar="../static/images.png", submission_image='../static/images.png')
        Submission.objects.create(id=4, title="Riscatto negato.", description='Pensavo finalmente di avere tutto.',
                                  votes=17,
                                  avatar="../static/images.png", submission_image='../static/images.png')

    return render(request, 'main/home_view.html',
                  {'submissions': list(Submission.objects.values())})
