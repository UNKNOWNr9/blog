from django.contrib.auth import admin
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article, Category
from django.views.generic import ListView, DetailView


class ArticleListView(ListView):
    queryset = Article.objects.published()
    template_name = 'main/post.html'
    paginate_by = 1
    context_object_name = 'articles'


class DetailArticleView(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)
    template_name = 'main/articles_detail.html'


def home(request):
    return render(request, 'main/home.html')


def contact(request):
    return render(request, 'main/contact.html')


def about(request):
    return render(request, 'main/about.html')


class CategoryListView(ListView):
    template_name = 'main/category.html'
    paginate_by = 2
    context_object_name = 'category'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()



