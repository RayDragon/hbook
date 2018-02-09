from django.http import HttpResponse, HttpResponseRedirect, Http404
from google.oauth2 import id_token
from google.auth.transport import requests
from .models import Users


def check_user(request):
    if request.method != "POST": raise Http404
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

        if is_logged(request):
            if request.session.get('email', '#') != idinfo['email']:
                log_out(request)
                request.session['email'] = idinfo['email']
                if Users.objects.filter(email=idinfo['email']).count() < 1:
                    usr = Users()
                    usr.email = idinfo['email']
                    usr.gid = userid
                    usr.save()
                error = "Okay"
            else:
                error = "Already Logged"
        else:
            request.session['email'] = idinfo['email']
            error="Okay"
    except ValueError:
        # Invalid token
        pass
    return HttpResponse(error)


def head_hbook(request):
    return HttpResponseRedirect("/static/index.html")


def get_csrf(request):
    from templates.w3.pagemaker import load
    return HttpResponse(load("csrf.html", request, {}))


def get_logout(request):
    if request.method != "POST": raise Http404
    log_out(request)
    return HttpResponse("Done")


def log_out(request):
    del request.session['email']


def is_logged(request):
    return request.session.get('email', False)


def check_login(request):
    if request.method != "POST":raise Http404
    try:
        if is_logged(request):
            return HttpResponse("1")
    except:
            print("exception")
    return HttpResponse("0")
