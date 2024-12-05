from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#custom managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, default=None, related_name='children', on_delete=models.SET_NULL, verbose_name='زیر دسته')
    title = models.CharField(max_length=50, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(unique=True, verbose_name='آدرس')
    status = models.BooleanField(default=False, verbose_name='نمایش داده شود؟')
    position = models.IntegerField(unique=True, verbose_name='پوزیشن')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیشنویس'),
        ('p', 'منتشر شده'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name='نویسنده')
    title = models.CharField(max_length=30, verbose_name='عنوان')
    slug = models.SlugField(max_length=30, unique=True, verbose_name='آدرس')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='articles')
    description = models.TextField(max_length=1500, verbose_name='توضیحات')
    thumbnail = models.ImageField(upload_to="Images", verbose_name='تصویر')
    published = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

    def category_published(self):
        return self.category.filter(status=True)

    objects = ArticleManager()