from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    allProjects = Project.objects.all() # selects everything from the Project table
    
    context = {
        'projects' : allProjects,
    }
    return render(request, 'main/index.html', context)

# detail page
def detail(request, id):
    project = Project.objects.get(id=id) # Selects everything from the Project table where id=id

    context = {
        "project" : project,
    }
    return render(request, 'main/details.html', context)

# add projects to the database
def add_projects(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST or None)

        # check if form is valid
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('main:home')
    else:
        form = ProjectForm()
    return render(request, 'main/addprojects.html', {"form":form})