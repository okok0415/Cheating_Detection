# Generated by Django 3.0 on 2021-03-30 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='user',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
