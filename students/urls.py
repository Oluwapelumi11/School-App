from django.urls import path
from . import views

app_name="students"
urlpatterns = [
    path('',views.StudentListView.as_view(),name='index'),
    path('<int:pk>/details',views.StudentDetailView.as_view(),name='details'),
]
