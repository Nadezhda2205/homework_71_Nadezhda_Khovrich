from random import choices
from django.contrib.auth.models import AbstractUser
from django.db import models




class Account(AbstractUser):

    SEX_CHOICES = [('M', 'мужской'), ('F', 'женский')] 
    avatar = models.ImageField(
        upload_to='avatars',
        verbose_name='Аватар',
        blank=True
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    about = models.TextField(
        null=True,
        blank=True,
        verbose_name='Информация'
    )
    phone = models.CharField(
        null=True,
        blank=True,
        verbose_name='Телефон',
        max_length=15

    )
    sex = models.CharField(
        choices=SEX_CHOICES,
        null=True,
        blank=True,
        verbose_name='Пол',
        max_length=1
    )
    subscriptions = models.ManyToManyField(
        verbose_name='Подписки', 
        to='accounts.Account', 
        related_name='subscribers',
        blank=True
        )


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
