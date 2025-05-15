from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class StudentData(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    city=models.CharField(max_length=122)
    country=models.CharField(max_length=122)
    pincode=models.CharField(max_length=10)
    linkedin=models.CharField(max_length=122,null=True)
    portfolio=models.CharField(max_length=122,null=True)
    person_desc=models.TextField(default="I am a front-end developer with more than 3 years of experience writing html, css, and js. I'm motivated, result-focused and seeking a successful team-oriented company with opportunity to grow.")
    date=models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class EducationData(models.Model):
    student = models.ForeignKey(StudentData, on_delete=models.CASCADE)
    institute_name=models.CharField(max_length=122)
    institute_location=models.CharField(max_length=122)
    degree=models.CharField(max_length=122)
    fieldOfStudy=models.CharField(max_length=122)
    graduation_month=models.CharField(max_length=122)
    graduation_year=models.CharField(max_length=122)


    def __str__(self):
        return f"{self.student.firstname} {self.institute_name}"

class SkillsData(models.Model):
    student = models.ForeignKey(StudentData, on_delete=models.CASCADE)
    project_name=models.CharField(max_length=122,default="DSP")
    project_desc=models.TextField(default="I am a front-end developer with more than 3 years of experience writing html, css, and js. I'm motivated, result-focused and seeking a successful team-oriented company with opportunity to grow.")
    skills=models.TextField()



    def __str__(self):
        return f"{self.student.firstname}"


