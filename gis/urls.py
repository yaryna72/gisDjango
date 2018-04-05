
"""djanng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls.py/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.conf.urls import url
import gis.views

urlpatterns = [
    url(r'^$', gis.views.home, name='home'),
    url(r'^map/$', gis.views.mymap, name='map'),
    url(r'^about/$', gis.views.about, name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', gis.views.show_articles, name='article'),

]
