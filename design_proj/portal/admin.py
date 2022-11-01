from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Request, Category

AdvUser = get_user_model()

admin.site.register(AdvUser)


@admin.register(Request)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary', 'category', 'photo_file')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
