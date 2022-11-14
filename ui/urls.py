from django.urls import path
from . import views

urlpatterns = [
  path('ping/', views.sayHello.say_hello),
  path('students/', views.students.handleStudentsReq)
]
 