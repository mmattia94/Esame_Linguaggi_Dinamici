from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from Campionato_Calcio.models import Opzioni
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def mainpage(request):
    options_list = Opzioni.objects.all()
    context = {'options_list': options_list}
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # create a new user and log them in immediately
            new_user = form.save()
            personal = User(user=new_user)
            personal.save()
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, new_user)
            return HttpResponseRedirect("/enter/")
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, "registration/register.html", context)


def logoutuser(request):
    logout(request)
    return HttpResponseRedirect("/Campionato/")

