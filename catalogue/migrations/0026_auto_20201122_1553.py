# Generated by Django 2.2.6 on 2020-11-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0025_auto_20201120_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='date_sown',
            field=models.DateField(blank=True, help_text='Date acquired, or date sown if from seed.', null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='sowing_method',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.DeleteModel(
            name='SpeciesInstance',
        ),
    ]
