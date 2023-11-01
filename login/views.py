from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "signin_page_pam.html")
