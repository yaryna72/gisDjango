
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from gis.models import Articles
# Create your views here.
def home(request):
    # return HttpResponse("Hello world")
    # return render(request, 'gis/home.html')
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'gis/home.html', context)


def show_articles(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    return render(request, 'gis/article.html', {'article': article})


def about(request):
    return render(request, 'gis/about.html')


def mymap(request):
    return render(request, 'gis/map.html')
