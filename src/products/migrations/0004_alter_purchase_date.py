# Generated by Django 4.0.2 on 2022-02-22 18:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 22, 18, 1, 7, 904902, tzinfo=utc)),
        ),
    ]
