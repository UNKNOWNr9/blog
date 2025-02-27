from django.urls import path
from blog.views import *
urlpatterns = [
       path('', HomePageView.as_view(), name='home'),
       path('post/', PostListView.as_view(), name='post-list'),
       path('post_detail/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
