# Generated by Django 4.0.2 on 2022-04-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_remove_project_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='post_image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]