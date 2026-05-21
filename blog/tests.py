from django.test import TestCase, Client
from django.urls import reverse, resolve
from .models import Post, Author, Tag
from .views import index, posts, post_detail, authors, author_detail, tags, tag_posts


# ─── TESTS DE MODELS ──────────────────────────────────────────────────────────

class AuthorModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            first_name="Maria",
            last_name="Garcia",
            email="maria@example.com"
        )

    def test_author_creation(self):
        self.assertEqual(self.author.first_name, "Maria")
        self.assertEqual(self.author.last_name, "Garcia")
        self.assertEqual(self.author.email, "maria@example.com")

    def test_author_str(self):
        self.assertEqual(str(self.author), "Maria Garcia")

    def test_author_email_unique(self):
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            Author.objects.create(
                first_name="Joan",
                last_name="Lopez",
                email="maria@example.com"  # email duplicat
            )


class TagModelTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(caption="django")

    def test_tag_creation(self):
        self.assertEqual(self.tag.caption, "django")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "django")

    def test_tag_unique(self):
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            Tag.objects.create(caption="django")  # duplicat


class PostModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            first_name="Pere",
            last_name="Puig",
            email="pere@example.com"
        )
        self.tag = Tag.objects.create(caption="python")
        self.post = Post.objects.create(
            title="El meu primer post",
            excerpt="Aquest és un resum del post",
            slug="el-meu-primer-post",
            content="Contingut llarg del post aquí, amb prou text per passar la validació.",
            author=self.author
        )
        self.post.tags.add(self.tag)

    def test_post_creation(self):
        self.assertEqual(self.post.title, "El meu primer post")
        self.assertEqual(self.post.slug, "el-meu-primer-post")

    def test_post_str(self):
        self.assertEqual(str(self.post), "El meu primer post")

    def test_post_author_relation(self):
        self.assertEqual(self.post.author, self.author)

    def test_post_tag_relation(self):
        self.assertIn(self.tag, self.post.tags.all())

    def test_post_slug_unique(self):
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            Post.objects.create(
                title="Altre post",
                excerpt="Resum de l'altre post",
                slug="el-meu-primer-post",  # slug duplicat
                content="Contingut de l'altre post",
                author=self.author
            )

    def test_related_name_posts(self):
        """L'autor ha de tenir el post via related_name 'posts'."""
        self.assertIn(self.post, self.author.posts.all())


# ─── TESTS D'URLS ─────────────────────────────────────────────────────────────

class URLsTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            first_name="Anna",
            last_name="Roca",
            email="anna@example.com"
        )
        self.tag = Tag.objects.create(caption="test")
        self.post = Post.objects.create(
            title="Post de prova URL",
            excerpt="Resum del post de prova per a tests",
            slug="post-de-prova-url",
            content="Contingut del post de prova per a tests d'URL.",
            author=self.author
        )
        self.client = Client()

    def test_index_url_status(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_url_template(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "blog/index.html")

    def test_posts_url_status(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)

    def test_posts_url_template(self):
        response = self.client.get(reverse("posts"))
        self.assertTemplateUsed(response, "blog/post_list.html")

    def test_post_detail_url_status(self):
        response = self.client.get(
            reverse("post_detail", args=[self.post.slug])
        )
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_template(self):
        response = self.client.get(
            reverse("post_detail", args=[self.post.slug])
        )
        self.assertTemplateUsed(response, "blog/post_detail.html")

    def test_post_detail_404(self):
        response = self.client.get(
            reverse("post_detail", args=["slug-inexistent"])
        )
        self.assertEqual(response.status_code, 404)

    def test_authors_url_status(self):
        response = self.client.get(reverse("authors"))
        self.assertEqual(response.status_code, 200)

    def test_authors_url_template(self):
        response = self.client.get(reverse("authors"))
        self.assertTemplateUsed(response, "blog/authors_list.html")

    def test_author_detail_url_status(self):
        response = self.client.get(
            reverse("author_detail", args=[self.author.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_author_detail_url_template(self):
        response = self.client.get(
            reverse("author_detail", args=[self.author.id])
        )
        self.assertTemplateUsed(response, "blog/author_detail.html")

    def test_author_detail_404(self):
        response = self.client.get(
            reverse("author_detail", args=[9999])
        )
        self.assertEqual(response.status_code, 404)

    def test_tags_url_status(self):
        response = self.client.get(reverse("tags"))
        self.assertEqual(response.status_code, 200)

    def test_tags_url_template(self):
        response = self.client.get(reverse("tags"))
        self.assertTemplateUsed(response, "blog/tag_list.html")

    def test_tag_posts_url_status(self):
        response = self.client.get(
            reverse("tag_posts", args=[self.tag.caption])
        )
        self.assertEqual(response.status_code, 200)

    def test_tag_posts_url_template(self):
        response = self.client.get(
            reverse("tag_posts", args=[self.tag.caption])
        )
        self.assertTemplateUsed(response, "blog/tag_post.html")

    def test_tag_posts_404(self):
        response = self.client.get(
            reverse("tag_posts", args=["tag-inexistent"])
        )
        self.assertEqual(response.status_code, 404)


# ─── TESTS DE VISTES ──────────────────────────────────────────────────────────

class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(
            first_name="Laia",
            last_name="Mas",
            email="laia@example.com"
        )
        self.tag = Tag.objects.create(caption="web")

        for i in range(5):
            post = Post.objects.create(
                title=f"Post número {i + 1}",
                excerpt=f"Resum del post número {i + 1} per a tests",
                slug=f"post-numero-{i + 1}",
                content=f"Contingut del post {i + 1}. Text suficientment llarg.",
                author=self.author
            )
            post.tags.add(self.tag)

    def test_index_shows_max_3_posts(self):
        response = self.client.get(reverse("index"))
        self.assertLessEqual(len(response.context["posts"]), 3)

    def test_posts_view_shows_all_posts(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(len(response.context["posts"]), 5)

    def test_post_detail_context(self):
        response = self.client.get(
            reverse("post_detail", args=["post-numero-1"])
        )
        self.assertIn("post", response.context)
        self.assertEqual(response.context["post"].slug, "post-numero-1")

    def test_author_detail_context(self):
        response = self.client.get(
            reverse("author_detail", args=[self.author.id])
        )
        self.assertIn("author", response.context)
        self.assertIn("posts", response.context)
        self.assertEqual(response.context["author"], self.author)

    def test_tag_posts_context(self):
        response = self.client.get(
            reverse("tag_posts", args=["web"])
        )
        self.assertIn("tag", response.context)
        self.assertIn("posts", response.context)
        self.assertEqual(response.context["tag"].caption, "web")

    def test_index_url_resolves_correct_view(self):
        found = resolve("/")
        self.assertEqual(found.func, index)

    def test_posts_url_resolves_correct_view(self):
        found = resolve("/posts")
        self.assertEqual(found.func, posts)

    def test_authors_url_resolves_correct_view(self):
        found = resolve("/authors")
        self.assertEqual(found.func, authors)
