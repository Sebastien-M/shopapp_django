from django import forms
from django.core.validators import RegexValidator


class InfoForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(label='Age', widget=forms.TextInput(attrs={'class':'form-control'}))
    number = forms.CharField(label='Phone Number',
                             max_length=14,
                             validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number')],
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('You must be over 18 years old')
        return age
