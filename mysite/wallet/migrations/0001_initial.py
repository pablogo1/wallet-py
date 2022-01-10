# Generated by Django 4.0.1 on 2022-01-10 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=150)),
                ('current_balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TransationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category_type', models.CharField(choices=[('I', 'Income'), ('E', 'Expense')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField()),
                ('created_date', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('description', models.CharField(max_length=20)),
                ('notes', models.CharField(blank=True, max_length=200, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
                ('transaction_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.transationcategory')),
            ],
        ),
    ]