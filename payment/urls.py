from django.urls import path
from . import views

app_name="payments"
urlpatterns = [
    path("<str:ref>/pay",views.pay,name="pay"),
    path("<str:ref>/",views.verify_payment,name="verify_payment"),
]
