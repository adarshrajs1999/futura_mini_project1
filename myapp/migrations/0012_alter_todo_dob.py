# Generated by Django 5.0.3 on 2024-03-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_todo_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
