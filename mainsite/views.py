from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime

def homepage(request):
    
    posts = Post.objects.all()
    now = datetime.now()

    return render(request, 'index.html', locals())
