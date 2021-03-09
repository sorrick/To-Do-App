"Form representations of a model"
from django import forms
from django.forms import ModelForm

from .models import *

"form of the app"
class TaskForm(forms.ModelForm):

    title= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    class Meta:
        model = Task
        fields = '__all__'

