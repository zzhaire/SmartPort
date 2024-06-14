# Generated by Django 4.2.13 on 2024-06-11 03:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PortModels", "0005_alter_recordserver_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="berth",
            name="ship_id",
            field=models.CharField(default="未停放", max_length=50, verbose_name="当前停放船舶"),
        ),
        migrations.AlterField(
            model_name="berth",
            name="status",
            field=models.BooleanField(default=False, verbose_name="占用状态"),
        ),
    ]