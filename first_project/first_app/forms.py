from django import forms
from django.core import validators
from first_app.models import Webpage

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with z.")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)],
    )
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        if email != vemail:
            raise forms.ValidationError("Make sure emails match!")

class NewWebpageForm(forms.ModelForm):
    # Validations can go here
    class Meta:
        model = Webpage
        fields = '__all__'
