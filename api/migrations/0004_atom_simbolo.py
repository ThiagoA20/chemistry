# Generated by Django 3.2.4 on 2021-06-28 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_enetgy_level_atom_energy_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='atom',
            name='simbolo',
            field=models.CharField(default='Z', max_length=2),
        ),
    ]
