from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        INVESTIGATION = 'IN', 'Investigation'
        REJECTED = 'RJ', 'Rejected'
    title = models.CharField(max_length=250, verbose_name='عنوان')
    slug = models.SlugField(unique=True, max_length=250, verbose_name='آدرس', blank=True, null=True)
    body = models.TextField(max_length=5000, verbose_name='توضیحات')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    image = models.ImageField(upload_to="images/", verbose_name='تصویر')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name='وضعیت')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها   '