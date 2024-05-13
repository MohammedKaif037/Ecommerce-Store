from django import forms

from StoreApp.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'}),
            'message': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Message'}),
        }

from django import forms
from .models import ShippingInformation, PaymentInformation

class ShippingInformationForm(forms.ModelForm):
    class Meta:
        model = ShippingInformation
        fields = ['full_name', 'address', 'city', 'state_province', 'postal_code', 'country',]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Full Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'City'}),
            'state_province': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'State/Province'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Postal/ZIP Code'}),
            'country': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Country'}),
        }

class PaymentInformationForm(forms.ModelForm):
    class Meta:
        model = PaymentInformation
        fields = ['card_number', 'expiration_date', 'cvv', 'billing_address']
        widgets = {
            'card_number': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Card Number'}),
            'expiration_date': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Expiration Date'}),
            'cvv': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'CVV/Security Code'}),
            'billing_address': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Billing Address'}),
        }
