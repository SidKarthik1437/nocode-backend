# Generated by Django 4.1.3 on 2023-02-18 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_remove_project_date_created_user_username"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="projects",),
        migrations.AddField(
            model_name="user",
            name="projects",
            field=models.ManyToManyField(to="users.project"),
        ),
    ]
