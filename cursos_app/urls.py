from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_course', views.index),
    path('courses/destroy/<course_id>', views.destroy_page),
    path('destroy/<course_id>', views.destroy)
]
