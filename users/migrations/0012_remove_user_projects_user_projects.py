# Generated by Django 4.1.3 on 2023-02-18 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_remove_user_projects_user_projects"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="projects",),
        migrations.AddField(
            model_name="user",
            name="projects",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.project",
            ),
        ),
    ]
