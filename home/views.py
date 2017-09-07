from django.shortcuts import render
from .models import Blog


def get_blogs(request):
    ctx = {
        'blogs': Blog.objects.all().order_by('-created')
    }
    print(Blog.objects.get(id=1).title)
    return render(request, 'base.html', ctx)
