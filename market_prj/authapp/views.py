from django.contrib import auth
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import BuyerUserRegisterForm, BuyerUserLoginForm, BuyerUserEditForm, BuyerUserProfileEditForm, \
    BuyerUserProfile


def register(request):
    title = 'Регистрация'
    if request.method == 'POST':
        register_form = BuyerUserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = BuyerUserRegisterForm()
    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)


def login(request):
    title = 'Вход'
    login_form = BuyerUserLoginForm(data=request.POST or None)
    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main'))
    content = {'title': title, 'login_form': login_form, 'next': next, }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


@transaction.atomic()
def edit(request):
    title = 'Редактирование'
    if request.method == 'POST':
        edit_form = BuyerUserEditForm(request.POST, instance=request.user)
        profile_form = BuyerUserProfileEditForm(request.POST, instance=request.user.buyeruserprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = BuyerUserEditForm(instance=request.user)
        profile_form = BuyerUserProfileEditForm(instance=request.user.buyeruserprofile)
    content = {'title': title, 'edit_form': edit_form, 'profile_form': profile_form}
    return render(request, 'authapp/edit.html', content)
