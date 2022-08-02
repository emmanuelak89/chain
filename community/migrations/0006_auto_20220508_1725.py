# Generated by Django 3.2.12 on 2022-05-08 16:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0005_auto_20220508_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='uploaded',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 8, 17, 25, 31, 783146)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='blogpost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogpost', to='community.blogpost'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='uploaded',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 8, 17, 25, 31, 783146)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
