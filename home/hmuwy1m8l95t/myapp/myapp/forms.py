from django import forms


class contact_form(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='last name', max_length=100)
