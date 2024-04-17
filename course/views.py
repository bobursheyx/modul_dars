from django.shortcuts import render
from django.views import View
from .models import Course,Teacher,Speciality

class CourselistView(View):
    def get(self,request):
        courses = Course.objects.all()
        contex = {
            'courses':courses
        }
        return render(request, 'main/course.html',contex)



class SpecialityListView(View):
    def get(self,request):
        specialitys = Speciality.objects.all()
        contex = {
            'specialitys':specialitys,
        }
        return render(request, 'main/speciality.html',contex)


class TeacherViewlist(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        contex = {
            'teachers':teachers,
        }
        return render(request, 'main/teacher.html', contex)
