from django.contrib.auth import admin
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User


class ArticleListView(ListView):
    queryset = Article.objects.published()
    template_name = 'main/post.html'
    paginate_by = 3
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
    paginate_by = 3
    context_object_name = 'category'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()


class AuthorList(ListView):
    paginate_by = 2
    template_name = 'main/author_list.html'

    def get_queryset(self):
        username = self.kwargs.get('username')
        self.author = get_object_or_404(User, username=username)
        return self.author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context
