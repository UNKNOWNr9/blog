from django.db import models

# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    full_name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    message = models.TextField(max_length=2000, verbose_name='متن توضیحات')
    created_at = models.DateTimeField(auto_now_add=True)
    response = models.TextField(max_length=2000, verbose_name='پاسخ ادمین')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='آیا خوانده شده ؟')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'لیست پیام ها'
        verbose_name_plural = 'لیست پیام ها'