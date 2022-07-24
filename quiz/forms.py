from random import choices
from django import forms
import django_filters
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'email', 'password1', 'password2']

class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'name': ['icontains'],
        }

