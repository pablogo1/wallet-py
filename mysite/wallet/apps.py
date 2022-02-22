"""
Wallet app configuration
"""
from django.apps import AppConfig
from django.core.signals import request_finished


class WalletConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wallet"

    def ready(self) -> None:
        """Application ready"""
        from . import signals

        # request_finished.connect(signals.before_saving_account)
