# Generated by Django 2.0.6 on 2019-11-14 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MovieInformation',
            new_name='Movie',
        ),
    ]
