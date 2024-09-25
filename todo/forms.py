from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']
