from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from django.forms.widgets import SelectDateWidget
from .models import Profile
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.request = request
        self.user = None
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        self.user = authenticate(self.request, username=username, password=password)
        if not self.user:
            raise ValidationError('Неверный логин или пароль')
    def get_user(self):
        return self.user
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=False)  # Новое поле
    tel = forms.CharField(max_length=15, required=False)  # Новое поле
    birthday = forms.DateField(required=False, widget=SelectDateWidget(years=range(1900, 2023)))
    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('Пароли не совпадают!')
    def clean_username(self):
        username = self.cleaned_data['username']
        User = get_user_model()

        if User.objects.filter(username=username).exists():
            raise ValidationError('такой пользователь уже есть')
        return username

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'tel', 'birthday', 'image']
