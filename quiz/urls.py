from django.urls import path
from . import views
from .views import *

urlpatterns = [
  path('create/', CustomUserCreateView.as_view()),
  path('list/', CustomUserListView.as_view()),
  path('detail/<int:pk>', CustomUserDetailView.as_view()),
  path('create-group/', GroupCreateView.as_view()),
  path('list-group/', GroupListView.as_view()),
  path('detail-group/<int:pk>', GroupDetailView.as_view()),
  path('create-participant/', ParticipantCreateView.as_view()),
  path('list-participant/', ParticipantListView.as_view()),
  path('detail-participant/<int:pk>', ParticipantDetailView.as_view()),
  path('list-question/', QuestionListView.as_view()),
  path('answer/', ParticipantAnswerListView.as_view()),
  path('', Quiz.as_view(), name='quiz'),
  path('r/<str:topic>/', RandomQuestion.as_view(), name='random' ),
  path('q/<str:topic>/', QuizQuestion.as_view(), name='questions' ),
]

