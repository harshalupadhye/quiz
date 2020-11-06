from django.contrib import admin
from django.urls import path,include
from quiz import views
from django.conf.urls import url
app_name="student"
urlpatterns = [
    url(r'^$',views.Answers,name="answer"),
   
]