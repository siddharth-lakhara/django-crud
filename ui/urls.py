from django.urls import path
from . import views

urlpatterns = [
  # path('', views.home.home),
  path('ping/', views.sayHello.say_hello)
]
 