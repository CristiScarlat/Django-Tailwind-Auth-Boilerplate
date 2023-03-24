from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


@login_required(login_url='/login')
def index(request):
    print(request.user.is_authenticated)
    return render(request, 'index.html')


def register(request):
    print("signup")
    return render(request, 'registration/register.html')
