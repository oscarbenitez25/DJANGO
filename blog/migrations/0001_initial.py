import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=100,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=100,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
            options={
                "ordering": ["last_name", "first_name"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "caption",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
            ],
            options={
                "ordering": ["caption"],
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=150,
                        validators=[django.core.validators.MinLengthValidator(5)],
                    ),
                ),
                (
                    "excerpt",
                    models.CharField(
                        max_length=300,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="posts"),
                ),
                ("date", models.DateField(auto_now_add=True)),
                ("slug", models.SlugField(unique=True)),
                (
                    "content",
                    models.TextField(
                        validators=[django.core.validators.MinLengthValidator(20)]
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to="blog.author",
                    ),
                ),
                ("tags", models.ManyToManyField(blank=True, to="blog.tag")),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
    ]
