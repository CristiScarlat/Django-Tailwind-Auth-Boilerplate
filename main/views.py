from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def index(request):
    print(request.user.is_authenticated)
    return render(request, 'index.html')


def login(request):
    print("login")
    return
