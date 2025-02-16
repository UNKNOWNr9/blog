from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from blog.models import Post


# Create your views here.
class HomePageView(ListView):
    template_name = 'blog/index.html'
    queryset = Post.objects.filter(status='PB')
    paginate_by = 3

class PostListView(ListView):
    template_name = 'blog/post-list.html'
    queryset  = Post.objects.filter(status='PB')
    paginate_by = 6

class PostDetailView(DetailView):
    queryset = Post.objects.filter(status='PB')