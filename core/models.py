import uuid

from django.db import models


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    invoice_no = models.UUIDField(default=uuid.uuid4())
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.invoice_no}- {self.customer_name} - {self.date}"


class InvoiceDetails(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice')
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.FloatField()
    price = models.FloatField()

    @property
    def get_price(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.invoice}: {self.get_price}"
