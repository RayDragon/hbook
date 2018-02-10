from django.http import HttpResponse
import json


class Response:
    @staticmethod
    def json(data, status='success', status_message='done'):
        return HttpResponse(json.dumps({'status': status, 'status_message': status_message, 'data': data}))
