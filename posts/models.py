from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    description = models.CharField(verbose_name='Описание', null=False, blank=False, max_length=200)
    image = models.ImageField(verbose_name='Фото', null=False, blank=False, upload_to='posts')
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(), 
        related_name='posts', 
        null=False, 
        blank=False,
        on_delete=models.CASCADE
        )
    liked_users = models.ManyToManyField(
        verbose_name='Понравилось пользователям', 
        to='accounts.Account', 
        related_name='liked_posts'
        )
    created_at = models.DateTimeField(auto_now_add = True)
