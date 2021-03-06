from django.http import Http404
from hbook.models import Users
from .models import School
from hbook.response import Response


def create(request):
    if request.method != "POST" or not Users.is_logged(request):
        raise Http404
    if request.POST.get('type', '#') == 'school':
        if School.create_school(
                request.session['id'],
                request.POST.get('name', 'Name'),
                request.POST.get('address', 'Address...'),
                request.POST.get('details', 'Details...')) == 1:
            return Response.json({'School_Name': request.POST.get('name', 'Name')})
        else:
            return Response.json({}, 'failed', 'Limit exceeded')

    raise Http404


def get_list(request):
    # if request.method != "POST" or not Users.is_logged(request): raise Http404
    if request.POST.get('type', '#') == 'school':
        kind = request.POST.get('kind', 'all')
        if kind == 'all':
            a = School.list_all_school_details()
            return Response.json({'all_schools': a})
        elif kind == 'both':
            a = School.list_user_school_details(request.session['id'])
            b = School.list_all_school_details()
            return Response.json({'user_schools': a, 'all_schools': b})
    return Response.json({}, 'failed', 'wrong credentials:'+str(33))
