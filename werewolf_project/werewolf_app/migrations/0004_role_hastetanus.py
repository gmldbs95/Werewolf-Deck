# Generated by Django 2.2 on 2019-12-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf_app', '0003_role_isrolemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='hasTetanus',
            field=models.BooleanField(default=False),
        ),
    ]
