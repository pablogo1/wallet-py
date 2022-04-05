"""
Wallet app configuration
"""
from django.apps import AppConfig


class WalletConfig(AppConfig):
    """Wallet App configuration"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "wallet"

    def ready(self) -> None:
        """Application ready"""
        from . import signals
