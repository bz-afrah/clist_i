# Generated by Django 4.2.3 on 2023-11-11 01:29

from django.db import migrations
import pyclist.indexes


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0102_remove_account_ranking_acc_key_449bb8_gist'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='account',
            index=pyclist.indexes.GistIndexTrgrmOps(fields=['key', 'name'], name='ranking_acc_key_449bb8_gist'),
        ),
    ]
