# Generated by Django 4.0.2 on 2022-04-13 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_galleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='gallery',
            field=models.ManyToManyField(to='core.Galleryimage'),
        ),
    ]
