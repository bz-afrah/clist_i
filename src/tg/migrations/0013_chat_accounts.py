# Generated by Django 5.0.6 on 2024-07-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0131_account_matching'),
        ('tg', '0012_chat_thread_id_alter_chat_chat_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='accounts',
            field=models.ManyToManyField(blank=True, related_name='chats', to='ranking.account'),
        ),
    ]
