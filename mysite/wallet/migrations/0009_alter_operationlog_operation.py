# Generated by Django 4.0.1 on 2022-04-07 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0008_alter_operation_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationlog',
            name='operation',
            field=models.ForeignKey(db_column='operation_code', on_delete=django.db.models.deletion.CASCADE, to='wallet.operation'),
        ),
    ]
