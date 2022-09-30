
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from UserAuthentications_App.forms import UserRegisterForm

@login_required(login_url='/login/')
def home_view(request):
    context = {
        "user" : request.user
    }
    return render(request, 'home.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            messages.success(request, f"{username} account created successfully")
            return redirect('home')
        else:
            username = form.cleaned_data.get('username')
            messages.warning(request, f"{username} account not created")
            return redirect('register')
    else:
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request,'register.html', context)


