# Generated by Django 2.2.13 on 2020-12-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0007_chat_coders'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
