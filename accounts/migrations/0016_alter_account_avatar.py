# Generated by Django 4.1.2 on 2022-10-30 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_account_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(upload_to='avatars', verbose_name='Аватар'),
        ),
    ]