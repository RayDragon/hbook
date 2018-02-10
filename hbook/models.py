from django.db import models


class Users(models.Model):
    email = models.EmailField(max_length=80, null=False, unique=True)
    gid = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.email

    @staticmethod
    def create_account(email, gid):
        if Users.objects.filter(email=email).count() >=1:
            return False
        usr = Users()
        usr.email = email
        usr.gid = gid
        usr.save()
        return True

    @staticmethod
    def login(request, email):
        if Users.objects.filter(email=email).count() !=1:
            return False
        # request.session['email'] = email
        request.session['id'] = Users.objects.get(email=email).id
        return True

    @staticmethod
    def logout(request):
        # del request.session['email']
        del request.session['id']
        return True

    @staticmethod
    def is_logged(request):
        if request.session.get("id", "#") != "#":
            return True
        return False
