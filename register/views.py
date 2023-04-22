from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf
from .models import Profile
from .forms import LoginForm, UserRegistrationForm
from .forms import UserEditForm, ProfileEditForm


def user_login(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    args['login_error'] = 'Аккаунт удален'
                    return render(request, 'login.html', args)
            else:
                args['login_error'] = 'Пользователь не найден'
                return render(request, 'login.html', args)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logouts(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            login(request, new_user)
            return redirect('/')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'user_form': user_form,
                                                 'profile_form': profile_form})


def profile(request):
    return render(request, 'profile.html')


def profile_personal(request):
    return render(request, 'profile_personal.html')


