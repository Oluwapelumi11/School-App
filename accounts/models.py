from django.db import models

   

class Fee(models.Model):
    name = models.CharField(("Name"), max_length=50)
    is_mandatory = models.BooleanField(default=True)
    amount = models.DecimalField(("Amount in Naira"), max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
    
    