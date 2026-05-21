from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post, Author, Tag


def index(request):
    """Pàgina principal: mostra els 3 darrers posts."""
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts,
    })


def posts(request):
    """Llistat de tots els posts, ordenats descendentment per data."""
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/post_list.html", {
        "posts": all_posts,
    })


def post_detail(request, slug):
    """Detall d'un post. Retorna 404 si no existeix."""
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {
        "post": post,
    })


def authors(request):
    """Llistat de tots els autors."""
    all_authors = Author.objects.all()
    return render(request, "blog/authors_list.html", {
        "authors": all_authors,
    })


def author_detail(request, author_id):
    """Detall d'un autor i els seus posts. Retorna 404 si no existeix."""
    author = get_object_or_404(Author, pk=author_id)
    author_posts = author.posts.all().order_by("-date")
    return render(request, "blog/author_detail.html", {
        "author": author,
        "posts": author_posts,
    })


def tags(request):
    """Llistat de totes les tags."""
    all_tags = Tag.objects.all()
    return render(request, "blog/tag_list.html", {
        "tags": all_tags,
    })


def tag_posts(request, tag):
    """Posts filtrats per una tag. Retorna 404 si la tag no existeix."""
    tag_obj = get_object_or_404(Tag, caption=tag)
    tagged_posts = tag_obj.post_set.all().order_by("-date")
    return render(request, "blog/tag_post.html", {
        "tag": tag_obj,
        "posts": tagged_posts,
    })


def custom_404(request, exception):
    """Vista personalitzada per a errors 404."""
    return render(request, "blog/404.html", status=404)
