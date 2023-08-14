from django.db import models
import phonenumbers
from django.core.exceptions import ValidationError
import os



class UploadPath:
    @staticmethod
    def image(instance, filename):
        ext = filename.split(".")[-1]
        if ext in ['jpg', 'jpeg', 'svg', 'png']:
            folder = f'{instance._meta.model_name}s'  # Assuming model name is lowercase
            folder = os.path.join(folder, f'{instance.user.first_name}_{instance.user.last_name}')
            return os.path.join(folder, f'{instance}.{ext}')
        else:
            raise ValidationError('Please upload a valid Image file')

    @classmethod
    def file_upload_path(cls, instance, filename):
        ext = filename.split(".")[-1]
        if ext in ['pdf', 'doc', 'docx', 'xlsx', 'odt']:
            folder = f'{instance._meta.model_name}s'  # Assuming model name is lowercase
            folder = os.path.join(folder, f'{instance.user.first_name}_{instance.user.last_name}')
            file_path = os.path.join(folder, "files")
            return os.path.join(file_path, f'{instance.user.first_name}_{instance.user.last_name}.{ext}')
        else:
            raise ValidationError('Only pdfs, docs, xlxs, and odt documents are allowed')

class PhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 13
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        try:
            parsed_number = phonenumbers.parse(value, "NG")
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValidationError("Invalid phone number.")
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
            return formatted_number
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValidationError("Invalid phone number.")
