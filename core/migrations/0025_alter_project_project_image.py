# Generated by Django 4.0.2 on 2022-04-11 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_remove_project_post_image_project_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
