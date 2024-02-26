from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context= {
        'title': 'Home - Главная',
        'content': 'Магазин мебели'

    }

    return render(request, 'dzsite/index.html', context)
def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст',
    }
    return render(request, 'dzsite/about.html', context)