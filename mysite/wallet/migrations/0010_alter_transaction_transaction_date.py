# Generated by Django 4.0.1 on 2022-04-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0009_alter_operationlog_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateField(),
        ),
    ]
