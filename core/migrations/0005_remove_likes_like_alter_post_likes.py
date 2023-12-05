# Generated by Django 4.2.7 on 2023-12-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='like',
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]