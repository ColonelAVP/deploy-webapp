from django.shortcuts import render, redirect
from .models import Home, About, Category, Project, Profile, Gallery, Contact
from django.http import HttpResponse
# Create your views here.


def index(request):
    # HOME
    home = Home.objects.latest('updated')
    # ABOUT
    about = About.objects.latest('updated')
    # Profile
    profiles = Profile.objects.filter(about=about)
    # SKills
    categories = Category.objects.all()
    # Projects
    projects = Project.objects.all()
    # Gallery
    gallery = Gallery.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'projects': projects,
        'gallery': gallery,
    }
    if request.method=='POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return render(request, 'contact.html', context)

    return render(request, 'index.html', context)