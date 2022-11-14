# from django.shortcuts import render
from django.http import HttpResponsxe

def say_hello(request):
  return HttpResponse('pong')
  