from django import forms
from django.forms import ModelForm
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
