# Generated by Django 3.2.6 on 2021-08-06 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("journal", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="ip",
            field=models.GenericIPAddressField(default="127.0.0.1"),
            preserve_default=False,
        ),
    ]