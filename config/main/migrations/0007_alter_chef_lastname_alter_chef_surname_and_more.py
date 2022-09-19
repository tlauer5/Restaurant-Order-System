# Generated by Django 4.0.5 on 2022-06-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_order_billed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='lastname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='chef',
            name='surname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('unassigned', 'Unassigned'), ('in_progress', 'In Progress'), ('cooked', 'Cooked'), ('delivered', 'Delivered'), ('billed', 'Billed')], default='unassigned', max_length=20),
        ),
    ]
