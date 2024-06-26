# Generated by Django 5.0.4 on 2024-04-30 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("VMSapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PurchaseOrder",
            fields=[
                (
                    "po_number",
                    models.CharField(
                        max_length=50, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("order_date", models.DateTimeField()),
                ("delivery_date", models.DateTimeField(blank=True, null=True)),
                ("items", models.JSONField()),
                ("quantity", models.IntegerField()),
                ("status", models.CharField(max_length=20)),
                ("quality_rating", models.FloatField(blank=True, null=True)),
                ("issue_date", models.DateTimeField()),
                ("acknowledgment_date", models.DateTimeField(blank=True, null=True)),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="VMSapp.vendor"
                    ),
                ),
            ],
        ),
    ]
