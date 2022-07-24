from django.contrib import admin
from .models import *
from . import models

admin.site.register(CustomUser)
admin.site.register(Participant)
admin.site.register(ParticipantAnswer)

@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
	list_display = [ 'name', ]

@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
	list_display = [ 'id', 'title', ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [ 'answer_text', 'is_right' ]

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [ 'title', 'quiz', 'file']
    list_display = [ 'title', 'quiz', 'date_updated', 'file' ]
    inlines = [ AnswerInlineModel, ] 

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [ 'answer_text', 'is_right', 'question' ]
