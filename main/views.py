from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    query = request.GET.get('title')
    allProjects = None
    if query:
        allProjects = Project.objects.filter(name__icontains=query)
    else:
        allProjects = Project.objects.all() # selects everything from the Project table
    
    context = {
        'projects' : allProjects,
    }
    return render(request, 'main/index.html', context)

# detail page
def detail(request, id):
    project = Project.objects.get(id=id) # Selects everything from the Project table where id=id
    reviews = Review.objects.filter(comment=id).order_by('-comment')

    context = {
        "project" : project,
        "reviews" : reviews,
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
    return render(request, 'main/addprojects.html', {"form":form, "controller":"Add Project"})

# edit the project
def edit_projects(request, id):
    # get the projects linked with id
    project = Project.objects.get(id=id)

    # form check
    if request.method == 'POST':
        form = ProjectForm(request.POST or None, instance=project)
        # check if form is valid
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('main:detail', id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'main/addprojects.html', {"form":form, "controller":"Edit Project"})

# delete project
def delete_projects(request, id):
    # get the project by id
    project = Project.objects.get(id=id)

    # delete the project
    project.delete()
    return redirect("main:home")

# the reviews view
def add_review(request, id):
    if request.user.is_authenticated:
        project = Project.objects.get(id=id)
        if request.method == 'POST':
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST['comment']
                data.rating = request.POST['rating']
                data.user = request.user
                # data.project = project
                data.save()
                return redirect('main:detail', id)
        else:
            form = ReviewForm()
        return render(request, 'main/details.html', {"form":form})
    else:
        return redirect('accounts:login')

# edit reviews
def edit_review(request, project_id, review_id):
    if request.user.is_authenticated:
        project = Project.objects.get(id=project_id)
        review = Review.objects.get(project=project, id=review_id)

        # check if the review was done by a logged in user
        if request.user == review.user:
            # grant permissioon
            if request.method == 'POST':
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    if (data.rating > 10) or (data.rating < 0):
                        error = 'Out of range. Please select rating from 0 to 10'
                        return render(request, 'main/editreview.html', {"error":error})
                    else:
                        data.save()
                        return redirect('main:detail', project_id)
            else:
                form = ReviewForm(instance=review)
            return render(request, 'main/editreview.html', {"form":form})
        else:
            return redirect('main:detail', project_id)
    else:
        return redirect('accounts:login')

# delete review
def delete_review(request, project_id, review_id):
    if request.user.is_authenticated:
        project = Project.objects.get(id=project_id)
        review = Review.objects.get(project=project, id=review_id)

        # check if the review was done by a logged in user
        if request.user == review.user:
            # grant permission
            review.delete()
    else:
        return redirect('accounts:login')