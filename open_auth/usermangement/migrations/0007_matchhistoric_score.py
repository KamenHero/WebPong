# Generated by Django 4.2.10 on 2024-11-17 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermangement', '0006_matchhistoric_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchhistoric',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
