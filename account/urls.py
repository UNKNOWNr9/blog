from django.urls import path
from account.views import Test
urlpatterns = [
    path('test', Test.as_view())
]