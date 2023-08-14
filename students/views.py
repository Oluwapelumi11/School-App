from django.shortcuts import render
from django.views import generic
from .models import Student
# Create your views here.

class StudentListView(generic.ListView):
    context_object_name="students"
    def get_queryset(self):
        return Student.objects.all()

class StudentDetailView(generic.DetailView):
    context_object_name="student"
    model= Student