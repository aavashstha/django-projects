from django import forms
from .models import Task


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =  [
            'title',
            'description',
        ]


class TaskUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =  [
            'title',
            'description',
            'is_complete'
        ]