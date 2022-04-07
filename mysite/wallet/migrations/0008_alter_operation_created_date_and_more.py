# Generated by Django 4.0.1 on 2022-04-07 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0007_alter_transaction_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='operationlog',
            name='operation',
            field=models.ForeignKey(db_column='code', on_delete=django.db.models.deletion.CASCADE, to='wallet.operation'),
        ),
    ]