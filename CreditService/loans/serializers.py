from rest_framework import serializers
from .models import User, Loan, Billing, Repayment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['unique_user_id', 'aadhar_id', 'name', 'email', 'annual_income', 'credit_score']

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['id', 'user', 'loan_type', 'loan_amount', 'interest_rate', 'term_period', 'disbursement_date', 'status']

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ['user', 'billing_date', 'due_date', 'min_due_amount', 'principal_balance', 'apr', 'interest_accrued']

class RepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repayment
        fields = ['loan', 'amount_paid', 'payment_date']
