# Generated by Django 4.0.2 on 2022-03-21 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0010_remove_post_tag_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='category_name',
        ),
    ]
