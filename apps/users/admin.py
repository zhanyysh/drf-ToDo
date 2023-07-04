from django.contrib import admin
from apps.users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'age', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'phone_number', 'age', 'date_joined')
    list_per_page = 20
 