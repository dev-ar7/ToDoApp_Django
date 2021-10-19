from django import forms
from django import forms
from django.forms import ModelForm, fields, models, widgets

from .models import Task, Username

# Create Forms Below


class UsernameForm(forms.ModelForm):
    class Meta:
        model = Username
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': "Enter a username"}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        queryset = Username.objects.filter(username=username).count()

        if queryset > 0:
            raise forms.ValidationError(
                "This Username Is Already Taken! Try With A Different One U+1F600")
        return username


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['complete', 'date_of_creation', 'username']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "What's On Your Mind Today? "}),
            'description': widgets.TextInput(attrs={'placeholder': "Describe Your Task...", 'cols': 80, 'rows': 5}),
        }
