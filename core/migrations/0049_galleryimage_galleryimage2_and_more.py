# Generated by Django 4.0.2 on 2022-05-30 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_remove_project_category_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='galleryimage2',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='galleryimage3',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='galleryimage4',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='galleryimage5',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='galleryimage6',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='galleryimage',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
