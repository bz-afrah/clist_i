# Generated by Django 4.2.11 on 2024-06-09 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('clist', '0151_resource_set_matched_coders_to_members'), ('clist', '0152_remove_resource_set_matched_coders_to_members_and_more'), ('clist', '0153_alter_contest_set_matched_coders_to_members')]

    dependencies = [
        ('clist', '0150_contest_promotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='set_matched_coders_to_members',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
