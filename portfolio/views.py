from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'portfolio/home.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'post': post})

class post_create(CreateView):
    model= Post
    template_name = 'post_new.html'
    fields = '__all__' 
    success_url = reverse_lazy('home')