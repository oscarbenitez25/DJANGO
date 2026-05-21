from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["last_name", "first_name"]


class Tag(models.Model):
    caption = models.CharField(
        max_length=50,
        unique=True,
        validators=[MinLengthValidator(2)]
    )

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ["caption"]


class Post(models.Model):
    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)]
    )
    excerpt = models.CharField(
        max_length=300,
        validators=[MinLengthValidator(10)]
    )
    image = models.ImageField(
        upload_to="posts",
        null=True,
        blank=True
    )
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(
        validators=[MinLengthValidator(20)]
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date"]
