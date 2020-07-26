from django.shortcuts import render

# Create your views here.
post = [
    {
        'author': 'Florent',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': '26.07.2020'
    },
    {
        'author': 'Hans',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': '27.07.2020'
    }
]


def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# blog -> templates -> blog -> templates.html
