from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views import View
from .models import User, Loan, Payment
import uuid
from django.utils import timezone

class RegisterUserView(View):
    def get(self, request):
        return render(request, 'register_user.html')

    def post(self, request):
        data = request.POST
        try:
            user = User.objects.create(
                aadhar_id=data.get('aadhar_id'),
                name=data.get('name'),
                email=data.get('email'),
                annual_income=data.get('annual_income'),
                unique_user_id=uuid.uuid4()
            )
            return JsonResponse({'unique_user_id': str(user.unique_user_id)})
        except Exception as e:
            return HttpResponseBadRequest(f'Failed to register user: {str(e)}')

class ApplyLoanView(View):
    def get(self, request):
        return render(request, 'apply_loan.html')

    def post(self, request):
        data = request.POST
        try:
            user = User.objects.get(unique_user_id=data.get('unique_user_id'))
            loan_uuid = uuid.uuid4()
            loan = Loan.objects.create(
                user=user,
                loan_type=data.get('loan_type'),
                loan_amount=data.get('loan_amount'),
                interest_rate=data.get('interest_rate'),
                term_period=data.get('term_period'),
                disbursement_date=data.get('disbursement_date'),
                loan_id=str(loan_uuid)
            )
            return JsonResponse({'loan_id': loan.loan_id})
        except Exception as e:
            return HttpResponseBadRequest(f'Failed to apply for loan: {str(e)}')

class MakePaymentView(View):
    def get(self, request):
        return render(request, 'make_payment.html')

    def post(self, request):
        data = request.POST
        loan_id = data.get('loan_id')
        try:
            loan = Loan.objects.get(loan_id=loan_id)
            Payment.objects.create(
                loan=loan,
                amount=data.get('amount')
            )
            return JsonResponse({'message': 'Payment processed'})
        except Exception as e:
            return HttpResponseBadRequest(f'Failed to process payment: {str(e)}')

class GetStatementView(View):
    def get(self, request):
        return render(request, 'get_statement.html')

    def post(self, request):
        loan_id = request.POST.get('loan_id')
        if not loan_id:
            return HttpResponseBadRequest('Loan ID is required')

        try:
            loan = Loan.objects.get(loan_id=loan_id)
            past_transactions = loan.payment_set.values('payment_date', 'amount')
            upcoming_transactions = Payment.objects.filter(loan=loan, payment_date__gt=timezone.now()).values('payment_date', 'amount')
            return JsonResponse({
                'past_transactions': list(past_transactions),
                'upcoming_transactions': list(upcoming_transactions)
            })
        except Exception as e:
            return HttpResponseBadRequest(f'Failed to get loan statement: {str(e)}')


def home_view(request):
    return render(request, 'home.html')
