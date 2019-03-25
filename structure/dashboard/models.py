"""Define database models for use in the PostgreSQL server."""

from django.contrib.postgres import fields
from django.db import models


class Student(models.Model):
    """Student model: contains information used by the dashboard."""

    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=29)
    avatar = models.CharField(max_length=20000)
    reference_number = models.CharField(max_length=12)
    tutor = models.CharField(max_length=50)
    timetable = fields.JSONField()
    attendance = fields.JSONField()
    markbook = fields.JSONField()


class User(models.Model):
    """User model: contains information specific to user authorization."""

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=8, unique=True)
    password = models.CharField(max_length=20)
