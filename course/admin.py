from django.contrib import admin
from .models import Speciality,Teacher,Position,Course


admin.site.register(Speciality)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Position)