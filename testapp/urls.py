from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_questions/', views.get_questions, name='get_questions'),
]
