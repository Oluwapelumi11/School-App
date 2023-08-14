from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from misc.utils import UploadPath

class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(("Phone Number"))
    profile_image = models.ImageField(("Profile"), upload_to=UploadPath.image, height_field=None, width_field=None, max_length=None)
    

    class Meta:
        permissions =[
            ('parent_permission','Can perform action as a Parent')
        ]
    @property
    def children(self):
        return self.user.students.all()
    
    @property
    def total_fee(self):
        fee = 0
        for child in self.children:
            fee+=child.balance
        balance = fee - self.total_payment
        return balance
        
    def __str__(self):
        return self.user.username
