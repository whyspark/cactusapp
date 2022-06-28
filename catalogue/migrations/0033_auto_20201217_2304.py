# Generated by Django 2.2.6 on 2020-12-17 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0032_source_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='source',
            options={'ordering': ['purchase_date', 'name']},
        ),
        migrations.AddField(
            model_name='source',
            name='end_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='ten_day_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('SOWN', 'Sown'), ('ACTIVE', 'Active'), ('NO_RESULTS', 'No results'), ('NON-ARRIVAL', 'Did not arrive')], default='PENDING', max_length=20),
        ),
    ]