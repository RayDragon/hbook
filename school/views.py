from django.http import HttpResponse, Http404
from hbook.views import is_logged

def create(request):
    if request.method != "POST" and  not is_logged(request): raise Http404
    return HttpResponse();