# Generated by Django 4.0.5 on 2022-06-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_chef_lastname_alter_chef_surname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='table',
        ),
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.ManyToManyField(to='main.table'),
        ),
    ]
