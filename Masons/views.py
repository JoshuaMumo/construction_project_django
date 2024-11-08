from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request,'blog.html')

def blog_details(request):
    return render(request,'blog_details.html')

def contact(request):
    return render(request,'contact.html')

def projects(request):
    return render(request,'projects.html')
    
def project_details(request):
    return render(request,'project_details.html')

def services(request):
    return render(request,'services.html')

def service_details(request):
    return render(request,'service_details.html')

def starter_page(request):
    return render(request,'starter_page.html')

def master(request):
    return render(request,'master.html')

def register_user(request):
    return render(request,'authenticate/register_user.html',)