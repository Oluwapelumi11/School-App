from django.shortcuts import render
from .models import Classroom
from django.views import generic
# Create your views here.

class ClassDetailView(generic.DetailView):
        model = Classroom
        template_name = "test.html"

    