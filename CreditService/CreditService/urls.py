# CreditService/urls.py

from django.contrib import admin
from django.urls import path
from loans.views import RegisterUserView, ApplyLoanView, MakePaymentView, GetStatementView, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('apply-loan/', ApplyLoanView.as_view(), name='apply-loan'),
    path('make-payment/', MakePaymentView.as_view(), name='make-payment'),
    path('get-statement/', GetStatementView.as_view(), name='get-statement'),
    path('', home_view, name='home'),
]
