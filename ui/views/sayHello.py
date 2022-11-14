# from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def say_hello(request: HttpRequest):
  return HttpResponse('pong')
  