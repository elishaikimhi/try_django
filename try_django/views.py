from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
    home_title = "Welcome to try Django."
    qs = BlogPost.objects.all()[:5]
    context = {"title": home_title, "blog_list":qs }
    return render(request,"home.html", context)

def about(request):
    about_title = "about..."
    return render(request,"hello_world.html",{"title": about_title })

def contact(request):
    form = ContactForm(request.POST or None)
    contact_title = "we can't hear you..."
    if form.is_valid():
        print(form.cleaned_data)
    form = ContactForm()
    contact_title = "we can't hear you..."
    context = {
        "title": contact_title,
        'form': form 
        }
    return render(request,"form.html",context)