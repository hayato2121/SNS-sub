# Generated by Django 4.1.7 on 2023-03-17 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("snsapp", "0015_comment_parent"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="parent",
        ),
    ]
