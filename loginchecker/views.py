from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def login(request):
    ctx = {}
    return render(request, 'loginchecker/login.html', ctx)

def create(request):
    ctx = {}
    if request.method == 'GET':
        ctx['form'] = PostForm
        return render(request, 'loginchecker/whole.html', ctx)
    elif request.method == 'POST':
        Post.objects.create(login_date=timezone.now())
        return redirect(to='whole')
        
def whole(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'loginchecker/whole.html', ctx)

def delete(request, pk):
    ctx = {}
    if request.method == 'GET':
        instance = get_object_or_404(Post, id=pk)
        ctx['instance'] = instance
        return render(request, 'loginchecker/delete.html', ctx)
    if request.method == 'POST':
        Post.objects.filter(id=pk).delete()
        return redirect(to='whole')