# Generated by Django 3.2.4 on 2021-06-30 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_atom_simbolo'),
    ]

    operations = [
        migrations.AddField(
            model_name='atom',
            name='Atomic_number',
            field=models.IntegerField(default=0),
        ),
    ]
