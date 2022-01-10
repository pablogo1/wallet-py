from django.db import models

# Create your models here.
class Account(models.Model):
    """
    Represents an account.
    """
    name: str = models.CharField(max_length=20)
    description: str = models.CharField(
        max_length=150,
        blank=True,
        null=True
        )
    current_balance: int = models.IntegerField(default=0)

class TransationCategory(models.Model):
    """
    Represents a simple income/expense (transaction) category.
    """
    CATEGORY_TYPE = (
        ('I', 'Income'),
        ('E', 'Expense'),
    )
    name: str = models.CharField(max_length=20)
    category_type: str = models.CharField(max_length=1, choices=CATEGORY_TYPE)

class Transaction(models.Model):
    """
    Represents a transaction.
    """
    transaction_date = models.DateTimeField()
    created_date = models.DateTimeField()
    account: Account = models.ForeignKey(
        Account, 
        on_delete=models.CASCADE,
        blank=False
        )
    transaction_category: TransationCategory = models.ForeignKey(
        TransationCategory, 
        on_delete=models.CASCADE,
        blank=False
        )
    amount: int = models.IntegerField()
    description: str = models.CharField(
        max_length=20,
        blank=False
        )
    notes: str = models.CharField(
        max_length=200,
        blank=True,
        null=True
        )