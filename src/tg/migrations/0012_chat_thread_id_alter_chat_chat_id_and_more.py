# Generated by Django 4.2.3 on 2023-08-14 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0011_auto_20210703_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='thread_id',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='chat_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='chat',
            unique_together={('chat_id', 'thread_id')},
        ),
    ]
