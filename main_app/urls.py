from django.contrib import admin
from django.urls import path
from main_app import views
from .views import GeneratePdf

urlpatterns = [
    path("",views.index,name="home/"),
    path("build-resume/",views.build_resume,name="build-resume"),
    path("experience-level/",views.experience_level,name="experience-level"),

    path("student-template/",views.student_template,name="student-template"),
    path("worker-template/",views.professional_template,name="worker-template"),

    path('student_details/', views.student_details, name='details'),
    path('education-template/', views.education_template, name='education-template'),

    path('education-details/<int:id>/', views.education_details, name='education-details'),
    path('skills-details/<int:id>/', views.skills_details, name='skills-details'),

    path('skills-template/', views.skills_template, name='skills-template'),
    path('pdf/<int:id>/', GeneratePdf.as_view(), name='pdf'),

]