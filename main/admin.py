from django.contrib import admin, messages
from .models import Article, Category
from django.utils.translation import ngettext
from django.utils.html import format_html

@admin.action(description='پیشنویس پست های انتخاب شده')
def make_draft(self, request, queryset):
    updated = queryset.update(status="d")
    self.message_user(
        request,
        ngettext(
            "%d پست پیشنویس شد",
            "%d پست پیشنویس شدند.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


@admin.action(description='انتشار پست های انتخاب شده')
def make_published(self, request, queryset):
    updated = queryset.update(status="p")
    self.message_user(
        request,
        ngettext(
            "%d پست منتشر شد",
            "%d پست منتشر شدند.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category_to_str', 'published', 'status', 'thumbnail_tag')
    search_fields = ('title', 'description',)
    ordering = ('status', '-published')
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_draft, make_published]

    def category_to_str(self, obj):
        return ",".join([category.title for category in obj.category_published()])
    category_to_str.short_description = 'دسته بندی'

    def thumbnail_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px; border-radius: 5px"/>'.format(obj.thumbnail.url))
    thumbnail_tag.short_description = 'تصویر'

admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    search_fields = ('title',)
    ordering = ('position',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
