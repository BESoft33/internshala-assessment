from rest_framework import serializers
from .models import Invoice, InvoiceDetails


class InvoiceSerializer(serializers.ModelSerializer):
    invoice = serializers.StringRelatedField(many=True)
    class Meta:
        model = Invoice
        fields = ['date', 'invoice_no', 'customer_name', 'invoice']


class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetails
        exclude = ['id']
