# Generated by Django 2.2.6 on 2021-03-26 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0034_loggerdata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loggerdata',
            options={'ordering': ['device_id', '-timestamp']},
        ),
        migrations.AddField(
            model_name='loggerdata',
            name='lux',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loggerdata',
            name='humidity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loggerdata',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
