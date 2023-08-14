from django.db import models

from django.urls import reverse
from misc.models import Subject
from misc.utils import UploadPath
from phonenumber_field.modelfields import PhoneNumberField


from django_countries.fields import CountryField

class Student(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='students')
    reg_no = models.IntegerField(("Register No"))
    parent = models.ForeignKey("parents.Parent", on_delete=models.CASCADE, related_name='students', blank=True, null=True)
    parent_phone_number = PhoneNumberField(("Parent/Guardian Phone"))
    dob = models.DateField(("Date of Birth"), auto_now_add=True)
    address = models.CharField(("Address"), max_length=100)
    classroom = models.ForeignKey("classroom.Classroom", verbose_name=("Class"), on_delete=models.SET_NULL, blank=True, null=True)
    enrollment_date = models.DateField(("Enrollment Date"), auto_now_add=True)
    image = models.ImageField(("Profile Image"), upload_to=UploadPath.image, blank=True, null=True)
    emergency_contact1 = PhoneNumberField(("Emergency Contact 1"), blank=True, null=True)
    emergency_contact2 = PhoneNumberField(("Emergency Contact 2"), blank=True, null=True)
    parent_email = models.EmailField(("Parent Email"), max_length=254, blank=True, null=True)
    
    @property
    def get_fee(self):
        return self.classroom.class_fee

    @property
    def mandatory_fees(self):
        return self.classroom.mandatory_fees
    
    @property
    def optional_fees(self):
        return self.classroom.optional_fees

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    def get_absolute_url(self):
        return reverse("students:details", kwargs={"pk": self.pk})
    
    class Meta:
        permissions = [
            ("student_permission","Can perform actions as a Student")
        ]
    
    @property
    def get_60(self):
        return self.classroom.mandatory_fees_amount * 0.6
    @property
    def get_100(self):
        return self.classroom.mandatory_fees_amount






    