from django.urls import path
from . import views

app_name='quizapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
    path('select', views.select, name='select'),
    path('quiz/<int:num>', views.quiz, name='quiz'),
    path('Top', views.Top, name='Top'),
]
