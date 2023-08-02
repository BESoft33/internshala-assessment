from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import InvoiceDetails, Invoice


@receiver(post_save, sender=Invoice)
def create_invoice_detail(sender, instance, created, **kwargs):
    if created and 'details' in instance.__dict__:
        details_data = instance.__dict__.pop('details')
        InvoiceDetails.objects.create(invoice=instance, **details_data)

