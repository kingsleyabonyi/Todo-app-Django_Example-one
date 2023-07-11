from django import forms
from django.forms import ModelForm
from . models import Task


class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__" # includes all fields in form
        # fields('title', 'completed') #include particular fields of model in form

        