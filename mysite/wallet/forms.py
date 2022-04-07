"""
Wallet application forms
"""

from django.forms import ModelForm

from wallet.models import Transaction


class TransactionForm(ModelForm):
    """
    Transaction form
    """

    class Meta:
        """Meta for Transaction form"""
        model = Transaction
        fields = ['transaction_date', 'account',
                  'transaction_category', 'amount', 'description']
