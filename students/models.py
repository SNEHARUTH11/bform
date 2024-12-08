# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    usn = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    booklet_no = models.CharField(max_length=50)

    def __str__(self):
        return self.name

