from django.db import models


class Users(models.Model):
    email = models.EmailField(max_length=80, null=False, unique=True)
    gid = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.email
