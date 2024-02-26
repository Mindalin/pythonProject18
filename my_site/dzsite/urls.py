from django.contrib import admin
from django.urls import path
from dzsite import views
app_name = 'dzsite'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
