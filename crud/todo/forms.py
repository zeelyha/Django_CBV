from dataclasses import fields
from django import forms
from .models import TodoApp

#creating a form
class TodoappForm(forms.ModelForm):
    #create meta class
    class Meta:
        #specify model to be used
        model = TodoApp

        #specify fields to be used
        fields = [
            "title",
            "description",
        ]

