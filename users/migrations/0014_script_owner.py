# Generated by Django 4.1.3 on 2023-02-18 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_remove_user_projects_alter_project_name_script"),
    ]

    operations = [
        migrations.AddField(
            model_name="script",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
