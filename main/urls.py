from django.urls import path
from . import views
from .views import ArticleListView, DetailArticleView, CategoryListView
urlpatterns = [
    path('', views.home, name='home'),
    path('post/', ArticleListView.as_view(), name='post'),
    path('post/article/<slug:slug>/', DetailArticleView.as_view(), name='articles_detail'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category'),

]
