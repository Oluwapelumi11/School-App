from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Teacher
from misc.models import Subject

class TeacherForm(ModelForm):
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    )
    class Meta:
        model = Teacher
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
