# Generated by Django 3.0.4 on 2020-12-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0014_auto_20201212_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='updatednum_of_user_note',
        ),
        migrations.AddField(
            model_name='profile',
            name='updatednum_of_user_note',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]