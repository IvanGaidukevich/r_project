from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'created_at', 'updated_at', 'available')
    list_filter = ('available', 'price')
    list_editable = ('available', 'price')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
