from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login,logout
from .middelwares import auth,guest

# Create your views here.
@guest
def register_view(request):
    '''
    #steps 1: check method [POST,GET]
    #steps 2: if method is POST, create object of form and validate form data
    #steps 3: if form is valid, create a new user and log in the user
    # steps 4: if user is authenticated, redirect to dashboard page
    # steps 5: if user is not authenticated, render the registration form
    '''
    
    if request.method== 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')        
    else:
        initial_data={'username':'','password1':'','password2':''}
        form=UserCreationForm(initial=initial_data)
    return render(request,'auth/register.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    
    else:
        initial_data={'username':'','password':''}
        form=AuthenticationForm(initial=initial_data)
        
    return render(request,'auth/login.html',{'form':form})


@guest
def dashboard_view(request):
    return render(request,'auth/dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')