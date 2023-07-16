# Generated by Django 4.2.3 on 2023-07-15 05:55

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("company", models.CharField(max_length=100)),
                ("address1", models.CharField(max_length=100)),
                ("address2", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, region=None
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                (
                    "invoice_total",
                    models.DecimalField(
                        blank=True, decimal_places=2, editable=False, max_digits=6
                    ),
                ),
                ("create_date", models.DateField(auto_now_add=True)),
                (
                    "invoice_terms",
                    models.TextField(
                        blank=True,
                        default="NET 30 Days. Finance Charge of 1.5% will be             made on unpaid balances after 30 days.",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invoices.client",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InvoiceItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item", models.CharField(max_length=200)),
                ("quantity", models.IntegerField(default=0)),
                ("rate", models.DecimalField(decimal_places=2, max_digits=6)),
                ("tax", models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="invoices.invoice",
                    ),
                ),
            ],
        ),
    ]
