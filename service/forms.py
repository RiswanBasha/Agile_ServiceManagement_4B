from django import forms
from django.contrib.auth.models import User
from . import models

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']


class offerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class offerForm(forms.ModelForm):
    class Meta:
        model = models.offer
        fields = ['agreement_name', 'employee_name', 'provider_name', 'contact_person', 'external_person', 'rate']

class offerSalaryForm(forms.Form):
    salary=forms.IntegerField();


class RequestForm(forms.ModelForm):
    class Meta:
        model=models.Request
        fields = [
            'project_information',
            'start_date',
            'end_date',
            'work_location',
            'contract_period',
            'domain',
            'role',
            'experience',
            'technology',
            'further_skills',
            'upload_resume',
            'onsite_days',
            'remote_days',
        ]
        widgets = {
        'project_information':forms.Textarea(attrs={'rows': 3, 'cols': 30})
        }

class AdminRequestForm(forms.Form):
    #to_field_name value will be stored when form is submitted.....__str__ method of customer model will be shown there in html
    customer=forms.ModelChoiceField(queryset=models.Customer.objects.all(),empty_label="Customer Name",to_field_name='id')
    offer=forms.ModelChoiceField(queryset=models.offer.objects.all(),empty_label="offer Name",to_field_name='id')
    cost=forms.IntegerField()

class AdminApproveRequestForm(forms.Form):
    offer=forms.ModelChoiceField(queryset=models.offer.objects.all(),empty_label="Offers",to_field_name='id')
    cost=forms.IntegerField()
    stat=(('Pending','Pending'),('Released','Released'))
    status=forms.ChoiceField( choices=stat)


class UpdateCostForm(forms.Form):
    cost=forms.IntegerField()


class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['by','message']
        widgets = {
        'message':forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }

class AskDateForm(forms.Form):
    date=forms.DateField()


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
