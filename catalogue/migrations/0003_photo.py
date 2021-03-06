# Generated by Django 2.2.6 on 2020-11-14 00:16

from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20201015_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(height_field='height', upload_to='images/', verbose_name='Image', width_field='width')),
                ('caption', models.CharField(max_length=80, verbose_name='Caption')),
                ('height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Height')),
                ('width', models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Width')),
                ('date_taken', models.DateField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Species')),
            ],
            options={
                'ordering': ['date_taken'],
            },
        ),
    ]
