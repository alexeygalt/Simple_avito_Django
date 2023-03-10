# Generated by Django 4.1.5 on 2023-01-24 12:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ad",
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
                        max_length=200,
                        validators=[django.core.validators.MinLengthValidator(1)],
                        verbose_name="Название",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Цена",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=1000, null=True, verbose_name="Описание"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Картинка"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Объявление",
                "verbose_name_plural": "Объявления",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
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
                    "text",
                    models.TextField(
                        max_length=1000,
                        validators=[django.core.validators.MinLengthValidator(1)],
                        verbose_name="Текст",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "ad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ads.ad",
                        verbose_name="Объявление",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
                "ordering": ["-created_at"],
            },
        ),
    ]
