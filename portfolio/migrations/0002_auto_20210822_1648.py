# Generated by Django 3.2.6 on 2021-08-22 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Contact Section'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name_plural': 'Portfolio Section'},
        ),
        migrations.AlterModelOptions(
            name='testimonial',
            options={'verbose_name_plural': 'Testimonial Section'},
        ),
    ]
