# Generated by Django 5.0.3 on 2024-03-28 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_todo_data_remove_todo_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='bio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='todo',
            name='salary',
            field=models.IntegerField(),
        ),
    ]