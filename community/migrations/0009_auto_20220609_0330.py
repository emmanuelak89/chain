# Generated by Django 3.2.12 on 2022-06-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_auto_20220508_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/home-profile.jpg', null=True, upload_to='images/')),
                ('question', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='uploaded',
            field=models.DateTimeField(blank=True, default='2022-05-08 17:55:54.349667'),
        ),
    ]