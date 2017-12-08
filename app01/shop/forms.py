from django import forms
from django.core.validators import RegexValidator


class InfoForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='First Name', max_length=50)
    age = forms.IntegerField(label='Age')
    number = forms.CharField(label='Phone Number',
                             max_length=14,
                             validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number')])

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('You must be over 18 years old')
        return age
