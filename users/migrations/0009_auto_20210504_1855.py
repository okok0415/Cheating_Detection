# Generated by Django 3.0 on 2021-05-04 18:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210504_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.DateField(default=datetime.datetime(2021, 5, 4, 18, 55, 5, 695824)),
        ),
    ]
