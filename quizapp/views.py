from django.shortcuts import render
from django.shortcuts import redirect
from .models import QuizModelForm, SubModelForm
from .forms import SubModelFormAdd

# Create your views here.
def index(request):
    my_dict = {
        'insert_something': "something",
    }
    return render(request, 'quizapp/index.html', my_dict)

def info(request):
    infodata = QuizModelForm.objects.all()
    my_dict2 = {
        'title':'問題',
        'val':infodata,
    }
    return render(request, 'quizapp/info.html', my_dict2)

def select(request):
    data = QuizModelForm.objects.all()
    my_dic = {
        'title': 'test',
        'val': data,
    }
    return render(request, 'quizapp/select.html', my_dic)

def quiz(request, num):
    obj = QuizModelForm.objects.get(id=num)

    if (request.method == 'POST'):
        obj_sub = SubModelForm()
        info = SubModelFormAdd(request.POST, instance=obj_sub)
        info.save()
        return redirect(to='/select')

    quiz_dict = {
        'id': num,
        'quiz_val': obj,
        'form': SubModelFormAdd(),
    }

    return render(request, 'quizapp/quiz.html', quiz_dict)

def Top(request):
    return render(request, 'quizapp/Top.html', {})
