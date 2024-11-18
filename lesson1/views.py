from django.shortcuts import render
from . import models

# Create your views here.
def display(request):
    return render(request, 'welcome.html')

def displayModels(request):
    data = models.NewForm.objects.all()
    return render(request,'models.html', {'data': data})




