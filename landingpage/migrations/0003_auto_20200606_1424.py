# Generated by Django 3.0.6 on 2020-06-06 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0002_event_project'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
