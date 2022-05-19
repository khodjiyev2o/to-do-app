from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm


# Create your views here.



def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.success(request,('There was an error!'))
            return redirect('login')
    else:
        return render(request, 'members.html')






def logout_user(request):
    logout(request)
    messages.warning(request, ('You have been logged out!'))
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.success(request,('There was an error!'))

            return redirect('login')
    else:
        return render(request, 'members.html')




def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password = form.cleaned_data['password1']
            new_user=authenticate(password=password,username=username)
            login(request,new_user)
            return HttpResponseRedirect('/main')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
