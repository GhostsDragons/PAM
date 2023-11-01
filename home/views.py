from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, "landing.html")
    # return HttpResponse("This is homepage")
