# Generated by Django 3.0.6 on 2020-06-17 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bios', '0003_auto_20200617_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='enddate',
            field=models.CharField(default='n/a', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bio',
            name='startdate',
            field=models.CharField(default='n/a', max_length=255),
            preserve_default=False,
        ),
    ]
