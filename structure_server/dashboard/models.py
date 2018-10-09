"""Define database models for use in the PostgreSQL server."""

from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres import fields
from django.db import models


class Class(models.Model):
    """Class model: contains information about general student classes."""

    class_id = models.AutoField(primary_key=True)
    teacher = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    room = models.CharField(max_length=10)

    class Meta:
        db_table = "class"


class Form(models.Model):
    """Form model: contains information specific to student form rooms."""

    form_id = models.AutoField(primary_key=True)
    class_id = models.OneToOneField(Class, on_delete=models.CASCADE)
    form_group = models.CharField(max_length=10)
    hall_head = models.CharField(max_length=50)

    class Meta:
        db_table = "form"


class Student(models.Model):
    """Student model: contains information used by the dashboard."""

    student_id = models.AutoField(primary_key=True)
    form_id = models.ForeignKey(Form, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=29)
    avatar = models.CharField(max_length=20000)
    reference_number = models.CharField(max_length=12)
    tutor = models.CharField(max_length=50)
    timetable = fields.JSONField()
    attendance = fields.JSONField()
    markbook = fields.JSONField()

    class Meta:
        db_table = "student"


class User(PermissionsMixin, models.Model):
    """User model: contains information specific to user authorization."""

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ("password",)
    is_anonymous = False
    is_authenticated = True

    user_id = models.AutoField(primary_key=True)
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE)
    username = models.CharField(max_length=8, unique=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "user"
