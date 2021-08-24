# Generated by Django 3.2.6 on 2021-08-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=256, null=True, unique=True),
        ),
    ]