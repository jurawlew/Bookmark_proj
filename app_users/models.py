from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
        Attributes
    """
    last_name = None
    first_name = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'
        ordering = ['id']

    def __str__(self):
        return f'{self.email}'
