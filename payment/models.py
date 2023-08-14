from django.db import models

# Create your models here.
import secrets
from .paystack import Paystack

# Create your models here.
class Payment(models.Model):
    owner = models.ForeignKey("parents.Parent", verbose_name=("payment"), on_delete=models.CASCADE)
    payment_info = models.TextField(("Description"))
    price = models.DecimalField(("Price"), max_digits=10, decimal_places=2)
    ref = models.CharField(("Reference"), max_length=50, blank=True)
    verified = models.BooleanField(("Verified"),default=False)
    date_created =models.DateField(("Date Created"), auto_now_add=True)


    class Meta:
        ordering = ("-date_created",)
    def __str__(self):
        return f"Payment of {self.price} by {self.owner.user.first_name} {self.owner.user.last_name}"
    def save(self,*args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)[:50]
            similar_ref = Payment.objects.filter(ref=ref)
            if not similar_ref:
                self.ref =ref
        super().save(*args,**kwargs)
    
    def amount_value(self):
        return self.price*100
    def verify_payment(self):
        paystack=Paystack()
        status,message,result = paystack.verify_payment(self.ref,self.price)
        if status:
            if result['amount'] /100 == self.price:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False

