from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from .models import Student

@receiver(post_save, sender=Student)
def assign_parent_permission(sender, instance, created, **kwargs):
    if created:
        permission = Permission.objects.get(codename="student_permission")
        instance.user_permissions.add(permission)
