from django.db import models

# Create your models here.
class Answer(models.Model):
    questionId=models.IntegerField()
    ans=models.CharField(max_length=20)