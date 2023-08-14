from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from misc.models import Subject
from misc.utils import UploadPath
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django_countries.fields import CountryField

# Create your models here.

class Teacher(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(("Phone Number"))
    address = models.CharField(("Address"), max_length=100)
    country = CountryField()
    image= models.ImageField(("Profile Photo"), upload_to=UploadPath.image, height_field=None, width_field=None, blank=True,null=True)
    facebook_profile = models.URLField(("Facebook Profile Link"), max_length=200, null=True,blank=True)
    instagram_handle = models.CharField(("Instagram Handle"), max_length=100,null=True,blank=True)
    twitter_profile = models.URLField(("Twitter Profile Link"), max_length=200, null=True,blank=True)
    emergency_contact1= models.CharField(("Emergency Contact 1"), max_length=100,null=True,blank=True)
    emergency_contact2= models.CharField(("Emergency Contact 2"), max_length=100,null=True,blank=True)
    qualification = models.CharField(("Best Qualification"), max_length=50)
    resume = models.FileField(("Resume"), upload_to=UploadPath.file_upload_path, max_length=100)
    salary = models.PositiveIntegerField(("Salary"))
    subjects = models.ManyToManyField(Subject)
    description= models.TextField(("description"), default="Nice me!!!")
    date_of_employment=models.DateField(("Date of Employment"), auto_now_add=True)
    r = 'Reception'
    Pr = 'Primary school'
    sc = 'Secondary school'
    m = 'Male'
    f = 'Female'
    ma = 'Married'
    si= "Single"
    m_stat_choice=(
        ('married',ma),
        ('single',si),
    )
    gender_choice= (
        ('male', m),
        ('female', f),
    )
    date_of_birth=models.DateField(("Date Of Birth"), auto_now=False, auto_now_add=False)

    gender = models.CharField(choices=gender_choice, max_length=50, default=m)
    marital_status = models.CharField(choices=m_stat_choice, max_length=50, default=si)
    teacher_type_choices =(
        ('Reception',r),
        ('Primary_School',Pr),
        ('Secondary School',sc),
    )
    teacher_type = models.CharField(choices=teacher_type_choices,default=r,max_length=100)
    def __str__(self):
        pre_name = ""
        if self.gender=="female":
            if self.marital_status == "married":
                pre_name = "Mrs"
            else:
                pre_name= "Miss"
        elif self.gender =="male":
            if self.marital_status == "married":
                pre_name = "Mr"
            else:
                pre_name= "Master"


        return pre_name+" "+self.user.first_name
    
    def get_absolute_url(self):
        return reverse("teachers:details", kwargs={"pk": self.pk})

    class Meta:
        permissions = [
            ("teacher_permission", "Can perform actions as a teacher"),
        ]
