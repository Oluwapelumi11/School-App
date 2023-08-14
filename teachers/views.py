from .models import Teacher
from datetime import date
from django.views import generic
from .forms import TeacherForm



# Create your views here.
class IndexView(generic.ListView):
    context_object_name="teachers"
    def get_queryset(self):
        return Teacher.objects.all()

class DetailView(generic.DetailView):
    context_object_name="teacher"
    model= Teacher
    
class TeacherCreateView(generic.CreateView):
    model = Teacher,
    url = "teachers:detail"
    form_class= TeacherForm

class TeacherUpdateView(generic.UpdateView):
    fields = "__all__"
    model =Teacher
    



