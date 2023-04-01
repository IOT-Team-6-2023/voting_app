from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('candidateList/', views.candidate_list, name='candidate_list')
]