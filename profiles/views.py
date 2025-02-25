from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, get_user_model, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import LoginForm, RegisterForm, UpdateUserForm, UpdateProfileForm
def home(request):
    return render(request, 'profiles/home.html')
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profiles_home')
    return render(request, 'profiles/login.html', {'form': form})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            tel = form.cleaned_data['tel']
            birthday = form.cleaned_data['birthday']
            # создали пользователя
            User = get_user_model()
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            # создать Profile
            Profile.objects.create(user=user,
                email=email,
                tel=tel,
                birthday=birthday)
            # залогинить
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)
            return redirect('profiles_home')
        # проверка валидности формы
    return render(request, 'profiles/register.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('main')

@login_required
def profile(request):
    try:
        profile = request.user.profile  # Получаем профиль текущего пользователя
    except Profile.DoesNotExist:
        # Если профиль не существует, создаем новый профиль
        profile = Profile.objects.create(user=request.user)
        messages.info(request, 'Ваш профиль был создан. Пожалуйста, заполните информацию.')

    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=profile)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен!')
            return redirect('profiles_profile')

    return render(request, 'profiles/profile.html', {
        'profile': profile,
        'user_form': user_form,
        'profile_form': profile_form
    })