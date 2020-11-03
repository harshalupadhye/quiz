from django.db import models
from django.urls import reverse
# Create your models here.
class Users(models.Model):
    role=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("login")
class quizz(models.Model):
    name=models.CharField(max_length=20,default="no quiz")
    def __str__(self):
        return self.name
   
    def get_absolute_url(self):
        return reverse("createquestion")
class quizzQuestion(models.Model):
    quiz=models.ForeignKey(quizz,related_name="questions",on_delete=models.CASCADE)
    question=models.CharField(max_length=300,blank=False)
    option1=models.CharField(max_length=30,blank=False)
    option2=models.CharField(max_length=30,blank=False)
    option3=models.CharField(max_length=30,blank=False)
    option4=models.CharField(max_length=30,blank=False)
    ans=models.CharField(max_length=300,blank=False)
    def get_absolute_url(self):
        return reverse("createquestion")

