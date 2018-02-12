from django.http import HttpResponse, HttpResponseRedirect, Http404
from google.oauth2 import id_token
from google.auth.transport import requests
from .models import Users
from .response import Response


def check_user(request):
    if request.method != "POST": raise Http404
    error=""
    token = request.POST.get("id_token", "#")
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), "596099888829-6vvcos64bnlgs0nrltala1id8g1k40hb.apps.googleusercontent.com")

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo['sub']
        print("got the user id", userid, idinfo['email'])

        if Users.is_logged(request):
            if request.session.get('email', '#') != idinfo['email']:
                Users.logout(request)
        Users.create_account(idinfo['email'], userid)
        Users.login(request, idinfo['email'])
        error="Okay"
    except ValueError:
        pass
    return HttpResponse(error)


def usr_info(request):
    if not Users.is_logged(request):
        raise Http404
    return Response.json(Users.get_details(request.session['id']))


def head_hbook(request):
    return HttpResponseRedirect("/static/index.html")


def get_csrf(request):
    from templates.w3.pagemaker import load
    return HttpResponse(load("csrf.html", request, {}))


def get_logout(request):
    if request.method != "POST": raise Http404
    if Users.logout(request):
        return HttpResponse("Done")
    return HttpResponse("error occurred")


def log_out(request):
    del request.session['email']


def check_login(request):
    if request.method != "POST":raise Http404
    try:
        if Users.is_logged(request):
            return HttpResponse("1")
    except:
            print("exception")
    return HttpResponse("0")
