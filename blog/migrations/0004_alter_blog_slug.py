# Generated by Django 3.2.6 on 2021-08-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=256, unique=True),
        ),
    ]