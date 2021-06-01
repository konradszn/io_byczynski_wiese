from django.shortcuts import render

posts = [
    {
        'author': 'Konrad',
        'title': 'Recipe 1',
        'content': 'First recipe',
        'date_posted': 'May 31, 2021'
    },
    {
        'author': 'Maks',
        'title': 'Recipe 2',
        'content': 'Second recipe',
        'date_posted': 'May 31, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})