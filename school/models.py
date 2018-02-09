from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    details = models.TextField()

    def create_school(self, request):
        email = request.session['email']
