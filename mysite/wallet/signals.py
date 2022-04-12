"""
Wallet applications signals
"""
from django.core import serializers
from django.db.models.signals import post_save
from django.dispatch import Signal, receiver

from wallet import models

operation_created = Signal


@receiver(post_save, sender=models.OperationLog)
def after_saving_account(sender, instance: models.OperationLog, **kwargs):
    """After saving operation entry"""

    print(f"Saved operation: {instance.operation}")
    transaction_data = list(serializers.deserialize(
        'json', instance.operation_data))[0]
    transaction_data.save()

# def after_saving_operation(sender, **kwargs):
#     print("After save operation")
