# Generated by Django 3.1.14 on 2022-01-09 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clist', '0073_contest_related'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='related',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_set', to='clist.contest'),
        ),
    ]