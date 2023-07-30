# Generated by Django 3.1.14 on 2023-06-10 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('true_coders', '0054_auto_20230528_1859'),
        ('ranking', '0081_accountverification'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifiedAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranking.account')),
                ('coder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='true_coders.coder')),
            ],
            options={
                'unique_together': {('coder', 'account')},
            },
        ),
    ]