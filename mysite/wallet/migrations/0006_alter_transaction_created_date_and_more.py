# Generated by Django 4.0.1 on 2022-04-07 03:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_transaction_created_by_transaction_modified_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]