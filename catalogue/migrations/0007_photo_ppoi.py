# Generated by Django 2.2.6 on 2020-11-14 16:09

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_auto_20201114_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI'),
        ),
    ]
