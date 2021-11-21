# Generated by Django 1.11.28 on 2020-03-08 19:30
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("base", "0002_auto_20200322_1821"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=30)),
                (
                    "priority",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Lowest"),
                            (2, "Low"),
                            (3, "Normal"),
                            (4, "High"),
                            (5, "Highest"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.Project",
                    ),
                ),
                ("resources", models.ManyToManyField(to="base.Resource")),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="tag",
            unique_together={("slug", "project")},
        ),
    ]
