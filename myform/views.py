from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.

def form_view(request):
    form=RegistrationForm()
    data={'form': form}
    
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
           return render(request, 'forms/form.html',data)
        
        
        return render(request, 'forms/form.html',data)