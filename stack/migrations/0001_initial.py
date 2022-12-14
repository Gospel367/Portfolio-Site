# Generated by Django 4.0.2 on 2022-03-19 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('tags', models.CharField(choices=[('app_development', 'app_developmet'), ('website_development', 'website_development'), ('data_science', 'data_science'), ('networking', 'networking'), ('programming', 'program')], max_length=50)),
                ('description', tinymce.models.HTMLField()),
                ('content', django_quill.fields.QuillField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='stack.Category')),
            ],
        ),
    ]
