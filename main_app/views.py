
from django.shortcuts import render, HttpResponse, redirect
from .models import StudentData,EducationData,SkillsData
from datetime import datetime
from django.views.generic import View
from .utils import render_to_pdf
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    return render(request,"index.html")
def build_resume(request):
    return render(request,"building/working.html")

def experience_level(request):
    return render(request,"building/experience-level.html")

def student_template(request):
    return render(request,"building/student-template.html")
def education_template(request):
    return render(request,"building/education-template.html")
def skills_template(request):
    return render(request,"building/skills-template.html")

def student_details(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        city=request.POST.get('city')
        country=request.POST.get('country')
        pincode=request.POST.get('pincode')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        person_desc=request.POST.get('person_desc')
        linkedin=request.POST.get('linkedin')
        portfolio=request.POST.get('portfolio_web')
        student = StudentData(
            firstname=firstname,
            lastname = lastname,
            city =city,
            country = country,
            pincode = pincode,
            email = email,
            phone = phone,
            linkedin = linkedin,
            portfolio=portfolio,
            person_desc=person_desc,
            date=datetime.today())
        student.save()
        id=student.id
        my_object = get_object_or_404(StudentData, id=id)
        context={
            'my_object': my_object,
        }
        return render(request,"building/education-template.html",context)
        # return redirect("/")
    return render(request, "building/student-template.html")

def education_details(request,id):
    if request.method=="POST":
        student = StudentData.objects.get(id=id)
        institute_name = request.POST.get('institute_name')
        institute_location = request.POST.get('institute_location')
        degree = request.POST.get('degree')
        fieldOfStudy=request.POST.get('fieldOfStudy')
        graduation_month = request.POST.get('month')
        graduation_year=request.POST.get('year')
        education=EducationData(
            student=student,
            institute_name=institute_name,
            institute_location=institute_location,
            degree=degree,
            fieldOfStudy=fieldOfStudy,
            graduation_month=graduation_month,
            graduation_year=graduation_year
            )
        education.save()
        my_object = get_object_or_404(StudentData, id=id)
        context = {
            'my_object': my_object,
            'student:':True,
        }
        return render(request,"building/skills-template.html",context)
        # return redirect("/")
    return render(request, "building/education-template.html")
#
def skills_details(request,id):
    if request.method=="POST":
        student = StudentData.objects.get(id=id)
        skills=request.POST.get('skills')
        project_name=request.POST.get('project_name')
        project_desc=request.POST.get('project_desc')
        skill = SkillsData(
            student=student,
            skills=skills,
            project_desc=project_desc,
            project_name=project_name
        )
        skill.save()
        my_object = get_object_or_404(StudentData, id=id)
        context = {
            'my_object': my_object,
        }
        return render(request,"building/test.html",context)
        # return redirect("/")
    return render(request, "building/skills-template.html")

#personal_video
def professional_template(request):
    return render(request,"building/worker-template.html")




#pdf generation
# static pdf
# class GeneratePdf(View):
#     def get(self,request,*args,**kwargs):
#         pdf=render_to_pdf('report.html')
#         return HttpResponse(pdf,content_type='application/pdf')

#download with custom filename
# class GeneratePdf(View):
#     def get(self,request,*args,**kwargs):
#         pdf=render_to_pdf('report.html')
#         if pdf:
#             response=HttpResponse(pdf,content_type='application/pdf')
#             hi="Anus"
#             filename=f"Student{hi}.pdf"
#             content=f"inline; filename={filename}"
#             response['Content-Disposition']=content
#             return response
#         return HttpResponse("Page Not Found")

class GeneratePdf(View):
    def get(self,request,id,*args,**kwargs):
        # product = Product.objects.filter(id=id).first()
        personal_details=StudentData.objects.get(id=id)
        education_details=EducationData.objects.filter(student=personal_details).first()
        skills_details=SkillsData.objects.filter(student=personal_details).first()
        print(id)
        print(personal_details.city)
        print(education_details)
        print(skills_details.skills)
        skills=skills_details.skills.split(',')
        data={
            'firstname':personal_details.firstname,
            'lastname':personal_details.lastname,
            'city':personal_details.city,
            'country':personal_details.country,
            'email':personal_details.email,
            'phone':personal_details.phone,
            'person_desc':personal_details.person_desc,
            'institute_name':education_details.institute_name,
            'institute_location':education_details.institute_location,
            'degree':education_details. degree,
            'fieldOfStudy':education_details.fieldOfStudy,
            'graduation_month':education_details.graduation_month,
            'graduation_year':education_details.graduation_year,
            'skills':skills,
            'project_name':skills_details.project_name,
            'project_desc':skills_details.project_desc,
        }
        pdf=render_to_pdf('building/report.html',data)
        if pdf:
            response=HttpResponse(pdf,content_type='application/pdf')
            hi="Anus"
            filename=f"{personal_details.firstname}.pdf"
            content=f"inline; filename={filename}"
            response['Content-Disposition']=content
            return response
        return HttpResponse("Page Not Found")


