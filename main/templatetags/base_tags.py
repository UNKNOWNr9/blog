from django import template
from ..models import Category
register = template.Library()


@register.inclusion_tag("main/partials/category_navbar.html")
def category_navbar():
    return {
        'categories': Category.objects.filter(status=True),
    }