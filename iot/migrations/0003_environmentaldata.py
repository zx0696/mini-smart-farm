# Generated by Django 4.2 on 2023-07-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iot", "0002_delete_environmentaldata"),
    ]

    operations = [
        migrations.CreateModel(
            name="EnvironmentalData",
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
                ("time", models.DateTimeField()),
                ("temp", models.FloatField()),
                ("humi", models.FloatField()),
                ("co2", models.FloatField()),
                ("water_supply", models.FloatField()),
                ("water_supply_cumulative", models.FloatField()),
                ("light", models.FloatField()),
                ("light_cumulative", models.FloatField()),
                ("soil_moisture1", models.FloatField()),
                ("soil_moisture2", models.FloatField()),
                ("soil_moisture3", models.FloatField()),
            ],
        ),
    ]
