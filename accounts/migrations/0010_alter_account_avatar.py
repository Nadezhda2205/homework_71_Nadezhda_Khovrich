# Generated by Django 4.1.2 on 2022-10-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_account_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatars', verbose_name='Аватар'),
        ),
    ]