# Generated by Django 3.0.6 on 2021-01-18 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Social'),
        ),
    ]