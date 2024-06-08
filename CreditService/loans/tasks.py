from celery import shared_task
from .models import User
import csv
from datetime import date, timedelta
from decimal import Decimal

@shared_task
def calculate_credit_score(aadhar_id):
    user = User.objects.get(aadhar_id=aadhar_id)
    total_balance = 0
    
    with open('path_to_csv_file.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['AADHAR ID'] == aadhar_id:
                amount = Decimal(row['Amount'])
                if row['Transaction_type'] == 'CREDIT':
                    total_balance += amount
                elif row['Transaction_type'] == 'DEBIT':
                    total_balance -= amount

    # Calculate credit score based on total balance
    if total_balance >= 1000000:
        credit_score = 900
    elif total_balance <= 10000:
        credit_score = 300
    else:
        credit_score = 300 + ((total_balance - 10000) // 15000) * 10
        credit_score = min(900, max(300, credit_score))
    
    user.credit_score = int(credit_score)
    user.save()

   
