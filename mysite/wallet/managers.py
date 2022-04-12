""" Wallet application manager """

from wallet.models import Operation, OperationType
from wallet.signals import operation_created

# from signals import after_saving_operation


class OperationManager:
    """Allows to create and update operations."""

    def create_operation(self):
        """Creates a new operation"""
        new_operation = Operation()
        operation_created.send(sender=self.__class__, operation=new_operation)
