# Generated by Django 3.1.14 on 2023-03-11 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clist', '0098_remove_contesttag_is_series'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contesttag',
            name='contests',
        ),
        migrations.AddField(
            model_name='contest',
            name='series',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='clist.contesttag'),
        ),
    ]
