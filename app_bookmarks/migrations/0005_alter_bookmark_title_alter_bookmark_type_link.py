# Generated by Django 4.2.4 on 2023-08-21 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookmarks', '0004_alter_bookmark_date_change_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='title',
            field=models.CharField(db_index=True, max_length=500, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='type_link',
            field=models.CharField(db_index=True, max_length=500, verbose_name='Type link'),
        ),
    ]