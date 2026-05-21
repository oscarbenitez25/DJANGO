from django.contrib import admin
from .models import Post, Author, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date", "slug")
    list_filter = ("author", "tags", "date")
    search_fields = ("title", "content", "excerpt")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    date_hierarchy = "date"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)
    search_fields = ("caption",)
