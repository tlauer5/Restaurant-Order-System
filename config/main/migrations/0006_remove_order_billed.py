# Generated by Django 4.0.5 on 2022-06-16 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_order_billed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billed',
        ),
    ]