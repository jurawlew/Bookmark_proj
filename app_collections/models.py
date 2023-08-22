from django.db import models

from app_users.models import User


class Collection(models.Model):
    """
        Attributes
    """
    title = models.CharField(verbose_name='Title', max_length=50, db_index=True)
    description = models.TextField(verbose_name='Description', max_length=500)
    date_create = models.DateTimeField(verbose_name='Date time create', auto_now_add=True)
    date_change = models.DateTimeField(verbose_name='Date time change', auto_now_add=True)

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, related_name='collection')
    # links = models.ManyToManyField(Bookmark, verbose_name='Links', related_name='collections')

    def __str__(self):
        return f'{self.title}'
