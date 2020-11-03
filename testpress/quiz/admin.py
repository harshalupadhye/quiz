from django.contrib import admin
from quiz.models import Users,quizz,quizzQuestion

# Register your models here.
admin.site.register(Users)
admin.site.register(quizz)
admin.site.register(quizzQuestion)
