# Generated by Django 4.2.2 on 2023-07-19 12:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userspage", "0003_alter_order_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("Cash on Delivery", "Cash on Delivery"),
                    ("Esewa", "Esewa"),
                    ("Khalti", "Khalti"),
                ],
                max_length=200,
            ),
        ),
    ]
