from django.urls import path
from . import views
from .views import ArticleListView, DetailArticleView, CategoryListView, AuthorList
urlpatterns = [
    path('', views.home, name='home'),
    path('post/', ArticleListView.as_view(), name='post'),
    path('post/article/<slug:slug>/', DetailArticleView.as_view(), name='articles_detail'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('category/<slug:slug>/page/<int:page>', CategoryListView.as_view(), name="category"),
    path('author/<slug:username>', AuthorList.as_view(), name="author"),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name="author"),

]
