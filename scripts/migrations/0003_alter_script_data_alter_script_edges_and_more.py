# Generated by Django 4.1.3 on 2023-02-18 04:58

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("scripts", "0002_alter_script_data_alter_script_edges_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="script",
            name="data",
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="script",
            name="edges",
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="script",
            name="nodes",
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
