# Generated by Django 5.0.6 on 2024-06-07 14:32

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(max_length=20)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('term_period', models.IntegerField()),
                ('disbursement_date', models.DateField()),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='OPEN', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_user_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('aadhar_id', models.CharField(max_length=12, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('annual_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit_score', models.IntegerField(default=300)),
            ],
        ),
        migrations.CreateModel(
            name='Repayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.loan')),
            ],
        ),
        migrations.AddField(
            model_name='loan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.user'),
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_date', models.DateField()),
                ('due_date', models.DateField()),
                ('min_due_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('principal_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('apr', models.DecimalField(decimal_places=2, max_digits=5)),
                ('interest_accrued', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.user')),
            ],
        ),
    ]
