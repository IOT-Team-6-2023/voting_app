from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('candidateList/', views.candidate_list, name='candidate_list'),
    path('voteCandidate/', views.vote_candidate, name='vote_candidate'),
    path('votingAction/', views.votingAction, name='vote_candidate'),
]