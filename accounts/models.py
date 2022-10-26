from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар'
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    # subscriptions = models.ManyToManyField(verbose_name='Подписки', to='accounts.Account', related_name='subscribers')
    # commented_posts = models.ManyToManyField('Прокомментированные публикации', to='posts.Post', related_name='user_comments')



    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
