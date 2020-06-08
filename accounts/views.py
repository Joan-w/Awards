from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# registration
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        # check if the form is valid
        if form.is_valid():
            user = form.save()

            # get the new password
            new_password = form.cleaned_data.get('password1')

            # authenitacte the user
            user = authenticate(username=user.username, password=new_password)

            # login user
            login(request, user)

            return redirect('main:home')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {"form":form})