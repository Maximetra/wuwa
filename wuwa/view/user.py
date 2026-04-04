from django.contrib import messages

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from wuwa.form.UserForm import UserForm

def register_view(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        user = form.save()

        login(request, user)
        return redirect('progession_view')

    return render(request, '../templates/user/register.html', {
        'form': form
    })

def login_view(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('progession_view')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login_view')

    else:
        return render(request, '../templates/user/login.html', {
            'form': form
        })

def logout_view(request):
    logout(request)
    return redirect('progession_view')
