from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.models import Profile


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, min_length=3, required=True, label="Имя пользователя")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Подтверждение пароля")
    first_name = forms.CharField(max_length=30, min_length=3, required=True, label="Имя")
    last_name = forms.CharField(max_length=30, min_length=3, required=True, label="Фамилия")
    email = forms.EmailField(max_length=100, required=True, label="Email")
    birth_date = forms.DateField(widget=forms.DateInput, required=True, label="Дата рождения")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            profile = Profile.objects.get(user=user)
            profile.birth_date = self.cleaned_data["birth_date"]
            profile.save()
        return user

