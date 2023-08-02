from rest_framework import serializers
from .models import Invoice, InvoiceDetails


class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetails
        fields = ['description', 'quantity', 'unit_price', 'price']


class InvoiceSerializer(serializers.ModelSerializer):
    invoice = InvoiceDetailsSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['date', 'invoice_no', 'customer_name', 'invoice']

    def create(self, validated_data):
        invoice_details_data = validated_data.pop('invoice', None)
        instance = super().create(validated_data)
        if invoice_details_data:
            for details_data in invoice_details_data:
                InvoiceDetails.objects.create(invoice=instance, **details_data)
        return instance
