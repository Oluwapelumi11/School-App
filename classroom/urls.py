from django.urls import path
from . import views

app_name ="class"
urlpatterns =[
 path("<int:pk>/",views.ClassDetailView.as_view(),name="details"),   
]