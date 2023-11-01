from django.shortcuts import render

# Create your views here.


def swiping(request):
    return render(request, "swiping_pam.html")
