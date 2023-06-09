# Generated by Django 4.1.7 on 2023-03-17 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("snsapp", "0014_reply"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="snsapp.comment",
                verbose_name="親コメント",
            ),
        ),
    ]
