import json
from django.http import Http404, HttpRequest, HttpResponse
from ..models import StudentsList


def handleStudentsReq(request: HttpRequest) -> HttpResponse:
  if request.method == 'GET':
    return handleGetReq(request)
  elif request.method == 'POST':
    return handlePostReq(request)
  else:
    raise Http404('Invalid method')
    
def handleGetReq(request: HttpRequest) -> HttpResponse:
  allStudents = StudentsList.objects.all()
  allStudents_list =  list(allStudents.values())
  return HttpResponse(json.dumps(allStudents_list))

def handlePostReq(request: HttpRequest) -> HttpResponse:
  return HttpResponse('path working')

