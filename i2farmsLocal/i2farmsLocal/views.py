from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("this is homepage(this will be a login page)")
    return render(request, 'homepage.html')