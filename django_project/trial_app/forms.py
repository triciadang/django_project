from django import forms
from .models import Book
from django.core.validators import RegexValidator


class CreateBookForm(forms.Form):
	title = forms.CharField(max_length = 50)
	author = forms.CharField(max_length = 50)
	summary = forms.CharField(widget = forms.Textarea)
	your_email = forms.CharField(max_length=50, required= False, validators = [RegexValidator(regex='^[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+$', message = 'Email address must be letters, digits, underscores, and periods with one @ and at most 50 characters.')])

