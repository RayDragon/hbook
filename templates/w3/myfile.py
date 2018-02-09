import re
from django.http import HttpResponse, HttpResponseRedirect


class RMatch:
    regex_name = re.compile(r"^[^\W0-9_]+([ \-'‧][^\W0-9_]+)*?\Z", re.U)
    regex_email = re.compile(r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])''', re.U)

    @staticmethod
    def validate(test_name, regex):
        return regex.match(test_name) is not None


class FormReply:
    @staticmethod
    def error_response(message):
        return HttpResponse('{"result":"fail", "message":"'+message+'"}')

    @staticmethod
    def sucess_RespoindWithMessage(message):
        return HttpResponse('{"result":"pass", "headto":"#m", "message":"' + message + '"}')

    @staticmethod
    def sucess_RespondRefresh():
        return HttpResponse('{"result":"pass", "headto":"#r", "message":"' + 'none' + '"}')

    @staticmethod
    def sucess_RespondHeadTo(location):
        return HttpResponse('{"result":"pass", "headto":"'+location+'"}')

    @staticmethod
    def header(location):
        return HttpResponseRedirect(location)