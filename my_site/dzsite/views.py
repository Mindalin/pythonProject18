from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context= {
        'title': 'Home',
        'content': 'Главная страница магазина',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'bool': True,
        'is_authenticated': False,
    }

    return render(request, 'dzsite/index.html', context)
def about(request):
    return HttpResponse('About page')