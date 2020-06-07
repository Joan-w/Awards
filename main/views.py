from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    allProjects = Project.objects.all() # selects everything from the Project table
    
    context = {
        'projects' : allProjects,
    }
    return render(request, 'main/index.html', context)

def detail(request, id):
    project = Project.objects.get(id=id) # Selects everything from the Project table where id=id

    context = {
        "project" : project,
    }
    return render(request, 'main/details.html', context)