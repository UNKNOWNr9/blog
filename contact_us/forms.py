from django import forms

class ContactUsForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField