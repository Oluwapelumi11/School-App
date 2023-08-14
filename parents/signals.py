from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from students.models import Student
from .models import Parent

@receiver(post_save, sender=Student)
def create_parent_user(sender, instance, created, **kwargs):
    if created:
        parent_phone = str(instance.parent_phone_number)
        parent_username = (parent_phone + '@joanisrael').lower()
        parent_password = (instance.user.last_name + "pass").lower()

        # Check if a user with the same phone number already exists
        if User.objects.filter(username=parent_username).exists():
            parent = User.objects.get(username=parent_username)
            instance.parent = parent
            instance.save()
        else:
            # Create the parent user
            user = User.objects.create_user(
                username=parent_username,
                password=parent_password,
            )

            # Create the parent instance
            parent = Parent.objects.create(
                user=user,
                phone_number=instance.parent_phone_number
            )

            # Associate the parent with the student
            instance.parent = parent
            instance.save()
            parent_permission = Permission.objects.get(codename="parent_permission")
            parent.user.user_permissions.add(parent_permission)
