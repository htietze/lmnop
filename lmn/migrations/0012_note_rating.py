# Generated by Django 3.1.2 on 2020-12-11 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0011_auto_20201207_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='rating',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=3, null=True),
        ),
    ]