from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your username here...'
        }
    ))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your email here...'
        }
    ))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your password here...'
        }
    ))
    password_confirm = forms.CharField(label='Confirm Password', required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Repeat your password here...'
        }
    ))



class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your username here...'
        }
    ))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your password here...'
        }
    ))