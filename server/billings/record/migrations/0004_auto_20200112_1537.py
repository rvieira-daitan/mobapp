# Generated by Django 3.0.2 on 2020-01-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(verbose_name='record date'),
        ),
    ]