# Generated by Django 3.2.6 on 2021-09-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task3', '0003_alter_extendeduser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='firstname',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='lstname',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='number',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]
