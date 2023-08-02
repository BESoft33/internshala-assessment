# Generated by Django 4.2.4 on 2023-08-02 04:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_invoice_invoice_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_no',
            field=models.UUIDField(default=uuid.UUID('070efd97-047f-41ac-968d-1837aea6901a')),
        ),
        migrations.AlterField(
            model_name='invoicedetails',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='core.invoice'),
        ),
    ]
