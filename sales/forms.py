from django import forms    #import django forms
from django.contrib.auth.models import User

CHART__CHOICES = (          #specify choices as a tuple
   ('#1', 'Bar chart'),    # when user selects "Bar chart", it is stored as "#1"
   ('#2', 'Pie chart'),
   ('#3', 'Line chart')
   )
#define class-based Form imported from Django forms
class SalesSearchForm(forms.Form): 
   book_title= forms.CharField(max_length=120)
   chart_type = forms.ChoiceField(choices=CHART__CHOICES)

#RegistrationForm
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password")
        p2 = cleaned_data.get("confirm_password")

        if p1 != p2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data