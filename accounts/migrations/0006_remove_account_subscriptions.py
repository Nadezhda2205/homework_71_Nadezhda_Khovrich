# Generated by Django 4.1.2 on 2022-10-28 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_subscriptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='subscriptions',
        ),
    ]
