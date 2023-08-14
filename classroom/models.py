from django.db import models

# Create your models here.
class Classroom(models.Model):
    name = models.CharField(("Class Name"), max_length=50)
    teacher = models.ManyToManyField("teachers.Teacher", verbose_name=("Class Teachers"))
    class_fee = models.ManyToManyField("accounts.Fee", verbose_name=("Fees"),related_name="fee",blank=True)
        
    @property
    def mandatory_fees_amount(self):
        total =0
        for i in self.class_fee:
            if i.is_mandatory:
                total +=i.amount
        return total

    @property
    def optional_fees(self):
        return self.class_fee.get(is_mandatory=False)
    @property
    def mandatory_fees(self):
        return self.class_fee.get(is_mandatory=True)
    @property
    def optional_fees_amount(self):
        total =0
        for i in self.class_fee:
            if not i.is_mandatory:
                total +=i.amount
        return total
    def __str__(self):
        return self.name

        