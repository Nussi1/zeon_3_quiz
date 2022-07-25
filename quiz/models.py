from tabnanny import verbose
from tkinter import CASCADE
from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.db import models
from .managers import UserManager
from django.utils.translation import gettext_lazy as _


#--------------------USER-------------------------
class CustomUser(AbstractUser):
    username=None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    group = models.ForeignKey(Group, default=None, on_delete=models.DO_NOTHING, null=True)
    itog_ball = models.CharField(max_length=255, blank=True, null=True)
    rating = models.CharField(max_length=255, blank=True, null=True)
    passed_tests = models.IntegerField()

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

#--------------------PARTICIPANT-------------------------
class Participant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, default=None, on_delete=models.DO_NOTHING, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    login = models.EmailField(unique=True)
    # group_name = models.ForeignKey(Group, default=None, on_delete=models.CASCADE, null=True)
    itog_ball = models.IntegerField()
    passed_tests = models.IntegerField()

    def __str__(self):
        return self.login


#--------------------QUIZ-------------------------
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Quizzes(models.Model):

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    title = models.CharField(max_length=255, default=_(
        "New Quiz"), verbose_name=_("Quiz Title"))
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Updated(models.Model):

    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True

class Question(Updated):

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    SCALE = (
        (0, _('Easy')),
        (1, _('Medium')),
        (2, _('hard')),
        (3, _('expert')),
    )

    TYPE = (
        (0, _('Multiple Choices')),
    )

    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, default=None, on_delete=models.DO_NOTHING, null=True)
    technique = models.IntegerField(
        choices=TYPE, default=0, verbose_name=_("Type of Question"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    file = models.FileField(upload_to='media/', blank=True )
    difficulty = models.IntegerField(
        choices=SCALE, default=0, verbose_name=_("Difficulty"))
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))
    qwty_questions = models.IntegerField(default=0)
    qwty_participants = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class Answer(Updated):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(
        max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)
    finished_time = models.IntegerField(default=20)
    ball = models.IntegerField(default=100)


    def __str__(self):
        return self.answer_text

# class Test(models.Model):
#     title = models.ForeignKey(Quizzes, default=None, on_delete=models.DO_NOTHING, null=True)
#     group = models.ForeignKey(Group, default=None, on_delete=models.DO_NOTHING, null=True)
#     question = models.ForeignKey(Question, default=None, on_delete=models.DO_NOTHING, null=True)




class ParticipantAnswer(models.Model):
    participant = models.ForeignKey(Participant, default=None, on_delete=models.DO_NOTHING, null=True)
    question = models.ForeignKey(Question, default=None, on_delete=models.DO_NOTHING, null=True)
    ownanswer = models.ForeignKey(Answer, default=None, on_delete=models.DO_NOTHING, null=True)
    time_spent = models.IntegerField(default=0)
    participant_ball = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.participant