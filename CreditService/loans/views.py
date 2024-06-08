from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views import View
from .models import User, Loan, Payment
import uuid

class RegisterUserView(View):
    def get(self, request):
        return render(request, 'register_user.html')

    def post(self, request):
        data = request.POST
        user = User.objects.create(
            aadhar_id=data['aadhar_id'],
            name=data['name'],
            email=data['email'],
            annual_income=data['annual_income'],
            unique_user_id=uuid.uuid4()
        )
        return JsonResponse({'unique_user_id': str(user.unique_user_id)})

class ApplyLoanView(View):
    def get(self, request):
        return render(request, 'apply_loan.html')

    def post(self, request):
        data = request.POST
        try:
            user = User.objects.get(unique_user_id=data['unique_user_id'])
            loan = Loan.objects.create(
                user=user,
                loan_type=data['loan_type'],
                loan_amount=data['loan_amount'],
                interest_rate=data['interest_rate'],
                term_period=data['term_period'],
                disbursement_date=data['disbursement_date'],
                loan_id=uuid.uuid4()
            )
            return JsonResponse({'loan_id': str(loan.loan_id)})
        except User.DoesNotExist:
            return HttpResponseBadRequest('Invalid User ID')

class MakePaymentView(View):
    def get(self, request):
        return render(request, 'make_payment.html')

    def post(self, request):
        data = request.POST
        try:
            loan = Loan.objects.get(loan_id=data['loan_id'])
            Payment.objects.create(
                loan=loan,
                amount=data['amount']
            )
            return JsonResponse({'message': 'Payment processed'})
        except Loan.DoesNotExist:
            return HttpResponseBadRequest('Invalid Loan ID')

class GetStatementView(View):
    def get(self, request):
        return render(request, 'get_statement.html')

    def post(self, request):
        loan_id = request.POST.get('loan_id')
        if not loan_id:
            return HttpResponseBadRequest('Loan ID is required')

        try:
            loan = Loan.objects.get(loan_id=loan_id)
            past_transactions = loan.payment_set.values('date', 'principal', 'interest', 'amount_paid')
            upcoming_transactions = loan.upcoming_transactions.values('date', 'amount_due')
            return JsonResponse({
                'past_transactions': list(past_transactions),
                'upcoming_transactions': list(upcoming_transactions)
            })
        except Loan.DoesNotExist:
            return HttpResponseBadRequest('Invalid Loan ID')

def home_view(request):
    return render(request, 'home.html')
