# Generated by Django 5.1 on 2024-08-09 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='unique_id',
            field=models.CharField(default='f01db1b1625b4fe0b76a5ba6f0795641', max_length=32, unique=True),
        ),
    ]
