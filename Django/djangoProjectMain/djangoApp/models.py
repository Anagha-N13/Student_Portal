from django.db import models

# Create your models here.

class Student(models.Model):
    usn = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    branch = models.CharField(max_length=20)

    def __str__(self):
        return self.usn+ "_" +self.name