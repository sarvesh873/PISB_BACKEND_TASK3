# Generated by Django 3.2.6 on 2021-10-31 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extendeduser',
            old_name='phone_number',
            new_name='number',
        ),
    ]
