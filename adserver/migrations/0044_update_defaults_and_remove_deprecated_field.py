# Generated by Django 2.2.13 on 2020-11-20 01:13
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0043_render_pixel_default_false'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='paid_campaigns_only',
        ),
        migrations.AlterField(
            model_name='publisher',
            name='record_views',
            field=models.BooleanField(default=False, help_text='Record each ad view from this publisher to the database'),
        ),
    ]