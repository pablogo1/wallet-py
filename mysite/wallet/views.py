"""
Wallet application views
"""

from datetime import datetime

from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from wallet.forms import TransactionForm
from wallet.models import Operation, OperationLog, Transaction


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Main view of wallet app")


class TransactionHistoryView(generic.ListView):
    """
    wallet/transactions main view.
    A list of transactions with links to create and edit transactions.
    """

    template_name = 'transactions/index.html'
    context_object_name = 'transaction_history'

    def get_queryset(self):
        # transaction_list = [
        #     {
        #         "transaction_date": "10/01/2021",
        #         "transaction_type": "Expense",
        #         "description": "Lunch",
        #         "amount": "12.12"
        #     },
        #     {
        #         "transaction_date": "10/03/2021",
        #         "transaction_type": "Expense",
        #         "description": "Cinema",
        #         "amount": "58.12"
        #     }
        # ]
        transaction_list = Transaction.objects.order_by(
            "-transaction_date")[:10]
        return transaction_list


class TransactionDetailView(generic.DetailView):
    """
    wallet/transactions/{id} view
    The transaction detail view.
    """

    model = Transaction
    template_name = "transactions/detail.html"


def create_transaction_view(request: HttpRequest) -> HttpResponse:
    """ Create transaction view """

    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            user = User.objects.get(id=1)
            new_transaction: Transaction = form.save(commit=False)
            new_transaction.created_date = timezone.now()
            new_transaction.modified_date = timezone.now()
            new_transaction.created_by = user
            new_transaction.modified_by = user

            operation_log_entry: OperationLog = OperationLog()
            operation_log_entry.operation = Operation.objects.get(
                code="NEW_TRANSACTION")
            operation_log_entry.operation_data = serializers.serialize('json', [
                                                                       new_transaction])

            print(operation_log_entry.operation_data)
            operation_log_entry.save()

            return HttpResponseRedirect('/wallet/transactions')
    else:
        form = TransactionForm()

    return render(request, 'transactions/new.html', {
        'form': form
    })
