# Generated by Django 3.2.3 on 2021-05-31 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secapp', '0012_auto_20210531_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suspect_recognised',
            name='detect_time',
            field=models.CharField(help_text='Format: YYYY-MM-DD HH:MM:SS', max_length=100),
        ),
    ]
