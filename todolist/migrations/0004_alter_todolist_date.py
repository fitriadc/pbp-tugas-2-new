# Generated by Django 4.1 on 2022-09-28 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_todolist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
