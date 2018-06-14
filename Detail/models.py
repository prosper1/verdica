from django.db import models
from Account.models import Profile

# Create your models here.

class Details(models.Model):
	 profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	 score = models.CharField(max_length=6, blank=True)
	 complete_lessons = models.CharField(max_length=4, blank=True)

