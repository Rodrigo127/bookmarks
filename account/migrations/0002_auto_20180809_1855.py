# Generated by Django 2.0.5 on 2018-08-09 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='data_of_birth',
            new_name='date_of_birth',
        ),
    ]
