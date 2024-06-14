import os
import sys
import django
import random
from datetime import datetime, timedelta

# 设置 Django 环境
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SmartPort.settings")
django.setup()

from PortModels.models import OceanCurrent


def clear_ocean_current_data():
    OceanCurrent.objects.all().delete()
    print("Cleared all ocean current data")


def generate_ocean_current_data():
    clear_ocean_current_data()

    silt_conditions = ["正常", "轻度淤沙", "中度淤沙", "严重淤沙"]

    base_date = datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0
    )  # 当前日期
    for day in range(3):  # 最近三天
        for hour in range(24):  # 每小时
            recorded_at = base_date - timedelta(days=day, hours=hour)
            silt_condition = random.choice(silt_conditions)
            depth = round(random.uniform(5.0, 30.0), 2)
            ocean_current_id = f"ocean_current_{recorded_at.strftime('%Y%m%d%H')}"

            ocean_current = OceanCurrent(
                ocean_current_id=ocean_current_id,
                recorded_at=recorded_at,
                silt_condition=silt_condition,
                depth=depth,
            )
            ocean_current.save()
            print(f"Generated ocean current data for {recorded_at}")


if __name__ == "__main__":
    action = input("Enter 'generate' to generate data or 'clear' to clear the data: ").strip().lower()
    if action == 'generate':
        generate_ocean_current_data()
    elif action == 'clear':
        clear_ocean_current_data()
    else:
        print("Invalid action.")
