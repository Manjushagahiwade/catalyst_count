from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Add a password field
    is_active = forms.BooleanField(initial=True)  # Add is_active field
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email','password','is_active')  # Include the fields you want

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
