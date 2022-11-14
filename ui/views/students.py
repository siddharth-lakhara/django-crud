
from django.http import HttpRequest, HttpResponse

def handleStudentsReq(request: HttpRequest) -> HttpResponse:
  if request.method == 'GET':
    return handleGetReq(request)
  elif request.method == 'POST':
    return handlePostReq(request)  
    
def handleGetReq(request: HttpRequest) -> HttpResponse:
  return HttpResponse('path working')

def handlePostReq(request: HttpRequest) -> HttpResponse:
  return HttpResponse('path working')

