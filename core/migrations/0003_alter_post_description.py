# Generated by Django 4.2.7 on 2023-12-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
