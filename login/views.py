from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("loged in")
            # return render(request, "swipping_pam.html")
        else:
            return render(request, "signin_page_pam.html")
    else:
        return render(request, "signin_page_pam.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST[""]
    return render(request, "signup_page_pam.html")


def reset(request):
    return render(request, "forgot_password_pam.html")


@login_required(login_url="/")
def home(request):
    return render(request, "swipping_pam.html")
