# Generated by Django 3.2.6 on 2021-09-19 00:11

from django.db import migrations, models
import django.db.models.deletion
import djangoyearlessdate.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0035_auto_20210326_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoilType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composition', models.CharField(max_length=300)),
                ('treatment', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterModelOptions(
            name='source',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='species',
            name='difficulty',
            field=models.CharField(choices=[('VERY_EASY', 'Very easy'), ('EASY', 'Easy'), ('AVERAGE', 'Average'), ('SOME_DIFFICULTY', 'Some difficulty'), ('DIFFICULT', 'Difficult'), ('VERY_DIFFICULT', 'Very difficult')], default='AVERAGE', max_length=20),
        ),
        migrations.AddField(
            model_name='species',
            name='growing_season_end',
            field=djangoyearlessdate.models.YearlessDateField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='species',
            name='growing_season_start',
            field=djangoyearlessdate.models.YearlessDateField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='species',
            name='humidity',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='species',
            name='light',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='species',
            name='max_temp_c',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='species',
            name='min_temp_c',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='species',
            name='substrate',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='species',
            name='watering',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='soil_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sources', to='catalogue.soiltype'),
        ),
    ]
