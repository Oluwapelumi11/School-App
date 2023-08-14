from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from .models import Teacher

@receiver(post_save, sender=Teacher)
def assign_parent_permission(sender, instance, created, **kwargs):
    if created:
        permission = Permission.objects.get(codename="teacher_permission")
        instance.user.user_permissions.add(permission)
