from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Jibril',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'Sep 17, 2020',

    },
    {
        'author': 'Ali',
        'title': 'Blog Post 2',
        'content': 'second Post content',
        'date_posted': 'Sep 17, 2020',

    },
    {
        'author': 'Mohamed',
        'title': 'Blog Post 3',
        'content': 'third Post content',
        'date_posted': 'Sep 17, 2020',

    },
]


def Home(request):
    # return HttpResponse('<h1>Home</>')
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def About(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/about.html', context)
