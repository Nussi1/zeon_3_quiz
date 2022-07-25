from email.policy import default
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.views import APIView
from knox.views import LoginView as KnoxLoginView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly

#--------------------USER-------------------------
class CustomUserCreateView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer

class CustomUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer   
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # permission_classes = (IsAuthenticated,)
    permission_classes = (IsOwnerOrReadOnly, )
    filter_fields = ('groups')
    search_fields = ('first_name', 'last_name', 'phone')

class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer   
    queryset = CustomUser.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


#--------------------GROUP-------------------------
class GroupCreateView(generics.CreateAPIView):
    serializer_class = GroupSerializer
    
class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer   
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = ('groups')
    search_fields = ('name')

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer   
    queryset = Group.objects.all()


#--------------------PARTICIPANT-------------------------
class ParticipantCreateView(generics.CreateAPIView):
    serializer_class = ParticipantSerializer

class ParticipantListView(generics.ListAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer   
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # permission_classes = (IsAuthenticated,)
    # permission_classes = (IsOwnerOrReadOnly, )
    filter_fields = ('phone')
    search_fields = ('first_name', 'last_name', 'phone')

class ParticipantDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParticipantSerializer   
    queryset = Participant.objects.all()
    # permission_classes = (IsOwnerOrReadOnly, )

#--------------------QUIZ-------------------------
class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        # question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        question = Question.objects.filter(quiz=2)
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        # quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        quiz = Question.objects.filter(quiz=1)
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)

class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer   
    # filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # permission_classes = (IsAuthenticated,)
    # permission_classes = (IsOwnerOrReadOnly, )
    # filter_fields = ('quiz')
    # search_fields = ('first_name', 'last_name', 'phone')

class ParticipantAnswerListView(generics.ListAPIView):
    queryset = ParticipantAnswer.objects.all()
    serializer_class = ParticipantAnswerSerializer  

    def get_queryset(self):
        answer = ParticipantAnswer.objects.all()
        return answer


    
