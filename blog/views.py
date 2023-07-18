from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': "Vikas",
        'title': "Blog Post 1",
        'content': 'My Django learning Story',   
        'date_posted':'July 15, 2023'
    },
    {
        'author': "Jon Doe",
        'title': "Blog Post 2",
        'content': 'My React  learning Story',   
        'date_posted':'July 20, 2023'
    },
    
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html',{"title": "About"})
