from django.contrib import admin
from .models import *
from . import models

# admin.site.register(Participant)
admin.site.register(ParticipantAnswer)



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
  fields = []
  list_display = ['first_name', 'last_name', 'group', 'phone', 'email', 'rating', 'itog_ball', 'passed_tests']
  list_filter = ['first_name', 'last_name', 'phone', 'group']

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
  fields = []
  list_display = ['first_name', 'last_name', 'group', 'phone', 'login', 'itog_ball', 'passed_tests']
  list_filter = ['first_name', 'last_name', 'phone', 'group',]
  

@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
	list_display = [ 'name', ]

@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
	list_display = [ 'id', 'title', ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [ 'answer_text', 'is_right' ]
    max_num = 4
    min_num = 4
    can_delete = False

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [ 'quiz', 'group', 'title', 'file', 'is_active']
    list_display = [ 'title', 'quiz', 'date_updated', 'file' ]
    inlines = [ AnswerInlineModel, ] 

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [ 'answer_text', 'is_right', 'question' ]
