from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.post_detail, name="post_detail"),
    path("authors", views.authors, name="authors"),
    path("authors/<int:author_id>", views.author_detail, name="author_detail"),
    path("tags", views.tags, name="tags"),
    path("tags/<str:tag>", views.tag_posts, name="tag_posts"),
]
