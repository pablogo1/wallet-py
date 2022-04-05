"""
Wallet applications signals
"""
from django.db.models.signals import pre_save
from django.dispatch import Signal, receiver

from wallet import models

operation_created = Signal

# @receiver(pre_save, sender=models.Account)
# def before_saving_account(sender, **kwargs):
#     """Before saving account"""
#     print("Saving...")


# def after_saving_operation(sender, **kwargs):
#     print("After save operation")
