from django.db import models

from app_collections.models import Collection
from app_users.models import User


class Bookmark(models.Model):
    """
        Attributes
    """
    title = models.CharField(verbose_name='Title', max_length=500, db_index=True)
    description = models.TextField(verbose_name='Description', max_length=500)
    link = models.TextField(verbose_name='Link', max_length=1000)
    type_link = models.CharField(verbose_name='Type link', max_length=500, db_index=True)
    image = models.FileField(verbose_name='Image', max_length=500, blank=True, null=True)
    date_create = models.DateTimeField(verbose_name='Date time create', auto_now_add=True)
    date_change = models.DateTimeField(verbose_name='Date time change', auto_now_add=True)

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, related_name='bookmark')
    collections = models.ManyToManyField(Collection, verbose_name='Collections', related_name='bookmarks')

    def __str__(self):
        return f'{self.title}'
