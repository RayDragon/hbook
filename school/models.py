from django.db import models


class School(models.Model):
    creatorId = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    address = models.TextField(null=True)
    details = models.TextField(null=True)

    @staticmethod
    def create_school(crid, name, address, details):
        if School.objects.filter(creatorId=crid).count()>5:
            return -1 # Limit exceeded

        sch = School()
        sch.creatorId = crid
        sch.name = name
        sch.address = address
        sch.details = details
        sch.save()
        return 1

    @staticmethod
    def list_user_school_details(crid):
        a = School.objects.filter(creatorId=crid)
        b=[]
        for sch in a:
            b.append({'id':sch.id, 'name':sch.name, 'address':sch.address, 'details':sch.details})
        return b

    @staticmethod
    def list_all_school_details():
        a = School.objects.all()
        b = []
        for sch in a:
            b.append({'id': sch.id, 'name': sch.name, 'address': sch.address, 'details': sch.details})
        return b


class Student(models.Model):
    'asdas'
    name = models.CharField(max_length=50, null=False)
    roll_number = models.CharField(max_length=20, null=False)


class Class(models.Model):
    name = models.CharField(max_length=20, null=False)


