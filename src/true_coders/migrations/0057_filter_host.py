# Generated by Django 4.2.3 on 2023-08-20 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('true_coders', '0056_alter_filter_start_time_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='host',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
