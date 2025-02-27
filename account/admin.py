from django.contrib import admin
from account.models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'get_full_name', 'phone_number')