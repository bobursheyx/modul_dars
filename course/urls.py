from django.urls import path
from .views import CourselistView,TeacherViewlist,SpecialityListView

urlpatterns = [
    path('course/',CourselistView.as_view(),name='courses'),
    path('teachers/',TeacherViewlist.as_view(),name='teachers'),
    path('specialities/',SpecialityListView.as_view(),name='specialities'),
]