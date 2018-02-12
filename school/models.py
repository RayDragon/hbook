from django.db import models
from myModules.fileDatabase import *

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

    def add_application(self, aid, app_as=1):
        f = MFile("applications", [15, 15, 3])
        f.insert_data([aid, self.id, app_as])
        f.file.close()

class Teacher(models.Model):
    school_ids = models.CommaSeparatedIntegerField()
    name = models.CharField(max_length=50, null=False)
    roll_number = models.CharField(max_length=20, null=False)
    lecture_ids = models.CommaSeparatedIntegerField()
    status = models.SmallIntegerField(default=-1)


class Student(models.Model):
    current_school_id = models.PositiveIntegerField(max_length=50, default=0)
    name = models.CharField(max_length=50, null=False)
    roll_number = models.CharField(max_length=20, null=False)
    group_ids=models.CommaSeparatedIntegerField()
    status = models.SmallIntegerField(default=-1)

    def apply_to_school(self, school_id):
        self.current_school_id = school_id


class Lecture(models.Model):
    name = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=50)
    time_from = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    repeat = models.SmallIntegerField()
    attendance = models.CommaSeparatedIntegerField()


class Group(models.Model):
    name = models.CharField(max_length=20, null=False)
    students = models.CommaSeparatedIntegerField()
    bytearray("asdasd")



