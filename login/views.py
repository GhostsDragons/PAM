from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "signin_page_pam.html")


def signup(request):
    return render(request, "signup_page_pam.html")


def fgtpwd(request):
    return render(request, "forgot_password_pam.html")
