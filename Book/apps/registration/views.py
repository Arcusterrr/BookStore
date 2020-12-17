from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .forms import RegistrForm


def registration(request):
    # try:
        data = {}
        if request.method == 'POST':
            form = RegistrForm(request.POST)
            if form.is_valid():
                form.save()
                data['form'] = form
                data['res'] = "Все прошло успешно"
                return render(request, 'login/registration.html', data)
        else:
            form = RegistrForm()
            data['form'] = form
            return render(request, 'login/registration.html', data)
    # except:
    #     Http404('Неизвестная ошибка')

def registrationAdd(request):
    try:
        data = {}
        if request.method == 'POST':
            form = RegistrForm(request.POST)
            if form.is_valid():
                form.save()
                data['form'] = form
                data['res'] = "Все прошло успешно"
                return render(request, 'main/registration.html', data)
        else:
            form = RegistrForm()
            data['form'] = form
            return render(request, 'main/registration.html', data)
    except:
        Http404('Неизвестная ошибка')