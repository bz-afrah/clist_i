# Generated by Django 3.1.14 on 2023-01-22 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clist', '0093_resource_has_upsolving'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='problem',
            index=models.Index(fields=['resource_id', 'key'], name='clist_probl_resourc_c3e019_idx'),
        ),
    ]
