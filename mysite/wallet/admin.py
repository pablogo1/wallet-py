"""
Wallet app admin module
"""
from django.contrib import admin

from wallet import models


# Register your models here.
class TransactionCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Account)
admin.site.register(models.TransactionCategory)
admin.site.register(models.Operation)
admin.site.register(models.OperationLog)
admin.site.register(models.Transaction)
