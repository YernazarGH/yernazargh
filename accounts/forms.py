from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class UserCreateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    password = forms.CharField(
        label='Пароль', strip=False,
        required=True, validators=[validate_password, ])
    password_confirm = forms.CharField(
        label='Повторите пароль', strip=False,
        required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password_confirm and password and password != password_confirm:
            raise ValidationError('Пароли не совпадают!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            self._save_m2m()
        return user

    class Meta:
        model = get_user_model()
        fields = [
            'username', 'password', 'password_confirm',
            'email', 'first_name', 'last_name', 'phone'
        ]
