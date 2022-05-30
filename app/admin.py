from django.contrib import admin
from .models import User
# Register your models re.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password']
    list_per_page = 3
    search_fields=('name',)
    list_filter=('name',)