from django.shortcuts import render

# Create your views here.


def swipping(request):
    return render(request, "swipping_pam.html")
