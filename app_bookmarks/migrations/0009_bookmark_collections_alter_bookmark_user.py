# Generated by Django 4.2.4 on 2023-08-21 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_collections', '0003_remove_collection_links'),
        ('app_bookmarks', '0008_alter_bookmark_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='collections',
            field=models.ManyToManyField(related_name='bookmarks', to='app_collections.collection', verbose_name='Collections'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmark', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
