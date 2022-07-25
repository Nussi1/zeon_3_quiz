from email.policy import default
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group


#--------------------GROUP------------------------------
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__" 


#--------------------USER-------------------------------
class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CustomUser
        fields=['first_name', 'last_name', 'groups', 'phone', 'email', 'password', 'itog_ball', 'rating']


#--------------------PARTICIPANT-------------------------
class ParticipantSerializer(serializers.ModelSerializer):
    # login = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Participant
        fields=['first_name', 'last_name', 'group', 'phone', 'login', 'itog_ball', 'passed_tests']


#--------------------QUIZ-------------------------------
class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizzes
        fields = "__all__" 

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = "__all__" 

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = "__all__" 

class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Question
        fields = "__all__" 


#--------------------RASCHET_BALLA-----------------------
best_finishing_time = 20
ball_default = 100
ne_proiden = 0
class ParticipantAnswerSerializer(serializers.ModelSerializer):

    raschet_balla = serializers.SerializerMethodField('_get_itog_ball')
    def _get_itog_ball(self, participantanswer_object):
        global ball_default
        global best_finishing_time
        global ne_proiden
        participant_ball = getattr(participantanswer_object, 'participant_ball')
        time_spent = getattr(participantanswer_object, 'time_spent')
        if time_spent == 1:
            participant_ball = (ball_default - (ball_default // best_finishing_time * time_spent) + (ball_default / best_finishing_time))
            return participant_ball
        elif time_spent >1 and time_spent <=20:
            participant_ball = (ball_default - (ball_default // best_finishing_time * time_spent))
            return participant_ball
        elif time_spent > best_finishing_time:
            return ne_proiden
        else:
            return ne_proiden

    class Meta:
        model = ParticipantAnswer
        fields = "__all__" 
        