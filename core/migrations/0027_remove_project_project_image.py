# Generated by Django 4.0.2 on 2022-04-11 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_project_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_image',
        ),
    ]
