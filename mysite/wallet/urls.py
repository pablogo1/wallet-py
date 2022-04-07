from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transactions', views.TransactionHistoryView.as_view(), name='transactions'),
    path('transactions/<int:pk>/', views.TransactionDetailView.as_view(),
         name="transaction_detail"),
    path('transactions/new', views.create_transaction_view,
         name='create_transaction')
]
