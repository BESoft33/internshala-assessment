from django.urls import path
from .views import InvoiceView, InvoiceItemView, InvoiceDetailsView, InvoiceItemDetailsView

urlpatterns = [
    path('invoices/', InvoiceView.as_view()),
    path('details/', InvoiceDetailsView.as_view()),
    path('invoices/<int:pk>', InvoiceItemView.as_view()),
    path('details/<int:pk>', InvoiceItemDetailsView.as_view())
]
