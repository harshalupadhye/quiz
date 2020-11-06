from django.shortcuts import render
from quiz.models import Users,quizz,quizzQuestion
from student.models import Answer
from quiz.forms import UsersForm
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.shortcuts import redirect
from django.template import Context, Template

# Create your views here.
def new_user(request):
    form=UsersForm()
    if request.method=='POST':
       
        form=UsersForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("user tried sigin and failed")
            # return HttpResponse("invalid credentials")
    return render(request,"signin.html",{'form':form})

    
def login(request):
    form=UsersForm()
    role=request.POST.get('role')
    name=request.POST.get('name')
    password=request.POST.get('password')
    if request.method=="POST":
        
        queryset = Users.objects.filter(name=request.POST.get("name")).values().first()
        print(queryset)
        if queryset['name']==name:

            if queryset['password']==password:
                if role=="teacher":
                    return redirect("menu")
                else:
                    return redirect("studentlist")
                
        else:
            return HttpResponse("not found")
    return render(request,"login.html",{'form':form})
class CreateQuizView(CreateView):
    model=quizz
    fields='__all__'
    template_name="quizz_form.html"
class QuizListView(ListView):
    context_object_name="quiz"
    model=quizz
    template_name="quizz_list.html"
class CreateQuestionView(CreateView):
    model=quizzQuestion
    fields='__all__'
    template_name="quizzquestion_form.html"
class QuizDetailView(DetailView):
    context_object_name="quiz"
    model=quizz
    template_name="quizz_detail.html"
def Menu(request):
    return render(request,"menu.html")
class QuizStudentListView(ListView):
    context_object_name="quiz"
    model=quizz
    template_name="quizzstudent_list.html"
class QuizStudentDetailView(DetailView):
    context_object_name="quiz"
    model=quizz
    template_name="quizzstudent_detail.html"
def Answers(request):
    if request.method=="POST":
        ans=Answer()
        template = Template("{{ q.question }}")
        context = Context({"q": q})
        questionId=request.POST.get('question')
        ans=request.POST.get('{{q.ans}}')
        print(template,context)
        


    
            
