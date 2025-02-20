# Generated by Django 4.2.13 on 2024-06-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PortModels", "0006_berth_ship_id_alter_berth_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recordberth",
            name="in_time",
            field=models.DateTimeField(blank=True, null=True, verbose_name="入港时间"),
        ),
        migrations.AlterField(
            model_name="recordberth",
            name="out_time",
            field=models.DateTimeField(blank=True, null=True, verbose_name="离港时间"),
        ),
    ]
