# Generated by Django 5.1.6 on 2025-02-15 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_alter_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='تصویر'),
        ),
    ]
