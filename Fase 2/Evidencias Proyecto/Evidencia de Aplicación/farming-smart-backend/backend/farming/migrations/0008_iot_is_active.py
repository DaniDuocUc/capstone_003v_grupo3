# Generated by Django 5.1.1 on 2024-10-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farming", "0007_delete_iotlog_remove_iot_battery_level_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="iot",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
