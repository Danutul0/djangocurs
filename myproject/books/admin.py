from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('date',)

