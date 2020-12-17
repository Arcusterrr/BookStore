from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login


def login_view(request):
    return render(request, 'login/authorization.html')

def authorization(request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            err = "Успешно"
            return render(request, 'login/authorization.html', {'error': err})
        else:
            err = "Ошибка аккаунта"
            return render(request, 'login/authorization.html', {'error' : err})
    else:
        err = "Неправильный логин или пароль"
        return render(request, 'login/authorization.html', {'error' : err})

def logout_view(request):
    try:
        logout(request)
    except KeyError:
        pass
    return HttpResponseRedirect('/')