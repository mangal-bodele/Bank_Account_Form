from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

        labels = {
            'cust_name': 'Account Holder Name',
            'account_no': 'Account Number',
            'dob': 'Date Of Birth',
        }

        widgets ={
            'cust_name' : forms.TextInput(attrs={'class':'form-control'}),
            'account_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'bank_name' : forms.TextInput(attrs={'class':'form-control'}),
            'branch_name' : forms.TextInput(attrs={'class':'form-control'}),
            'branch_code' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.Textarea(attrs={'rows':3,'class':'form-control'}),
            'dob' : forms.DateInput(attrs={'type':'date','class':'form-control'})
        }