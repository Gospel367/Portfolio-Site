# Generated by Django 4.0.2 on 2022-04-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_alter_project_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
