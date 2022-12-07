from django.shortcuts import render

# Create your views here.
def doctors_home(request):
    return render(request,'doctors_templates/home.html')