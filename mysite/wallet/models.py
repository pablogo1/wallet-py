"""
Wallet application models.
"""
from django.db import models


# Create your models here.
class Account(models.Model):
    """
    Represents an account.

    Attributes
    ----------
    name : CharField (max_length=20)
        Name of the account
    description : CharField (max_length=150, blank=True)
        A small and non-required description of the account
    current_balance : IntegerField(default=0)
        The account current balance. All money here is stored in cents.
        This is intended to be read-only and not modified by the user.
    """

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=150, blank=True, null=True)
    current_balance = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.name}"


class TransationCategory(models.Model):
    """
    Represents a simple income/expense (transaction) category.

    Attributes
    ----------
    name : CharField(max_length=20)
        Category name
    category_type = CharField(max_length=1)
        Category Type: E - Expense, I - Income
    """

    CATEGORY_TYPE = (
        ("I", "Income"),
        ("E", "Expense"),
    )
    name = models.CharField(max_length=20)
    category_type = models.CharField(max_length=1, choices=CATEGORY_TYPE)


class Transaction(models.Model):
    """
    Represents a transaction.

    Attributes
    ----------
    transaction_date : DateTimeField
        Date and time of when the transaction takes effect
    created_date : DateTimeField
        Date and time of when the transaction was created
    account : Account
        Account that this transaction affects
    transaction_category : TransactionCategory
        The transaction category this transaction applies to
    """

    transaction_date = models.DateTimeField()
    created_date = models.DateTimeField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False)
    transaction_category = models.ForeignKey(
        TransationCategory, on_delete=models.CASCADE, blank=False
    )
    amount = models.IntegerField()
    description = models.CharField(max_length=20, blank=False)
    notes = models.CharField(max_length=200, blank=True, null=True)
