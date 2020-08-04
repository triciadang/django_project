from django.db import models
from django.core.validators import RegexValidator

class Book(models.Model):
	title = models.CharField(max_length = 50)
	author = models.CharField(max_length = 50)
	summary = models.TextField()
	your_email = models.CharField(max_length = 50, null = True, blank = True)

