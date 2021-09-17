# Generated by Django 3.2.7 on 2021-09-17 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_be', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
    ]