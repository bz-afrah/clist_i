# Generated by Django 4.2.3 on 2023-11-12 09:56

from django.db import migrations, models

from clist.models import Contest


def set_n_problems(apps, schema_editor):
    for contest in Contest.objects.all():
        if hasattr(contest, 'stage'):
            continue
        contest.n_problems = len(list(contest.problems_list))
        contest.save(update_fields=['n_problems'])


class Migration(migrations.Migration):

    dependencies = [
        ('clist', '0128_resource_problems_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='n_problems',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AddIndex(
            model_name='contest',
            index=models.Index(fields=['resource', '-n_statistics'], name='clist_conte_resourc_f6d15f_idx'),
        ),
        migrations.AddIndex(
            model_name='contest',
            index=models.Index(fields=['resource', '-n_problems'], name='clist_conte_resourc_18d870_idx'),
        ),

        migrations.RunPython(set_n_problems),
    ]
