"""
Wallet applications signals
"""
from django.db.models.signals import pre_save
from django.dispatch import receiver

from wallet import models


@receiver(pre_save, sender=models.Account)
def before_saving_account(sender, **kwargs):
    """Before saving account"""
    print("Saving...")
