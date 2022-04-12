"""
Wallet application models.
"""
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Operation(models.Model):
    """
    Represents an Operation in the application.

    Attributes
    ----------
    code : CharField (max_length=20)
        Code of the operation
    description : CharField (max_length=150)
        Description of the operation.
    operation_data : JSONField()
        The operation data as a JSON document which will be used to process the operation
    active : BooleanField()
        Indicates if the operation is still active in the application to be processed.
    created_date : DateTimeField()
        The operation created date
    """

    code = models.CharField(max_length=20, blank=False,
                            db_index=True, unique=True, primary_key=True)
    description = models.CharField(max_length=150, blank=False)
    active = models.BooleanField(default=True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"({self.code}) {self.description} - {self.created_date}"


class OperationLog(models.Model):
    """
    Represents a log of operations performed in the application.

    Attributes
    ----------
    operation : ForeignKey()
        The operation reference.
    operation_data : JSONField()
        The operation data as a JSON document which will be used to process the operation
    created_date : DateTimeField()
        The date when the operation was logged into the application.
    """

    operation = models.ForeignKey(
        Operation, on_delete=models.CASCADE, blank=False, db_index=True, db_column="operation_code")
    operation_data = models.JSONField(blank=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.operation.code} - {self.created_date}"


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


class TransactionCategory(models.Model):
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

    def __str__(self) -> str:
        return f"{self.name} ({self.category_type})"


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
    description : CharField(max_length=50)
        Transaction description
    notes : CharField(max_length=200)
        Transaction notes
    """

    transaction_date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False)
    transaction_category = models.ForeignKey(
        TransactionCategory, on_delete=models.CASCADE, blank=False
    )
    amount = models.IntegerField()
    description = models.CharField(max_length=50, blank=False)
    notes = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, related_name="transaction_created_by_user")
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, related_name="transaction_modified_by_user")

    def __str__(self) -> str:
        return f"{self.transaction_category.name} - {self.description}: {self.amount} ({self.transaction_date})"
