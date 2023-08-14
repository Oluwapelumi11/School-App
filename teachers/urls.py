from django.urls import path
from . import views

app_name='teachers'
urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("<int:pk>/",views.DetailView.as_view(),name="details"),
    path("create/",views.TeacherCreateView.as_view(),name="create"),
    path("<int:pk>/update",views.TeacherUpdateView.as_view(),name="update"),

]
