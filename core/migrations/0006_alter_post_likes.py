# Generated by Django 4.2.7 on 2023-12-05 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_likes_like_alter_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
