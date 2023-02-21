from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.cat import Cat


def cat_stats_view(request: WSGIRequest):
    action = request.POST.get('action')
    Cat.action(action)
    Cat.name = request.POST.get('name', Cat.name)
    context = {
        'name': Cat.name,
        'age': Cat.age,
        'happiness': Cat.happiness,
        'fullness': Cat.fullness,
        'activity': Cat.activity,
    }
    return render(request, 'cat_stats.html', context=context)
