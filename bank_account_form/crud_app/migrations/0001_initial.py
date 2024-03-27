# Generated by Django 5.0.3 on 2024-03-25 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=20)),
                ('account_no', models.IntegerField()),
                ('account_type', models.CharField(choices=[('SAV', 'Saving'), ('CUR', 'Current'), ('FIX', 'Fixed'), ('DEM', 'Demat'), ('RECU', 'Recurring')], max_length=10)),
                ('bank_name', models.CharField(max_length=20)),
                ('branch_name', models.CharField(max_length=20)),
                ('branch_code', models.IntegerField()),
                ('address', models.CharField(max_length=20)),
                ('dob', models.DateField()),
            ],
        ),
    ]