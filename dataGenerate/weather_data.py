import os
import sys
import django
import random
from datetime import datetime, timedelta

# 设置 Django 环境
# 确保项目目录在 sys.path 中
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SmartPort.settings')
django.setup()

from PortModels.models import Weather

def clear_weather_data():
    Weather.objects.all().delete()
    print("Cleared all weather data.")

def generate_weather_data():
    descriptions = [
        ('晴朗', 'normal'),
        ('阴', 'normal'),
        ('小雨', 'normal'),
        ('中雨', 'alert'),
        ('台风', 'danger'),
        ('大雨', 'alert'),
        ('高温', 'alert'),
        ('暴雨', 'danger'),
        ('大雾', 'alert')
    ]

    base_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  # 使用当前日期
    for day in range(3):  # 最近三天
        for hour in range(24):  # 每小时
            recorded_at = base_date - timedelta(days=day) + timedelta(hours=hour)
            description, warning_level = random.choice(descriptions)
            temperature = round(random.uniform(-10, 35), 2)  # 生成 -10 到 35 之间的随机温度
            rainfall = round(random.uniform(0, 400), 2)  # 生成 0 到 50 之间的随机降雨量
            weather_id = f"weather_{recorded_at.strftime('%Y%m%d%H')}"

            weather = Weather(
                weather_id=weather_id,
                recorded_at=recorded_at,
                warning_level=warning_level,
                description=description,
                temperature=temperature,
                rainfall=rainfall
            )
            weather.save()
            print(f"Generated weather data for {recorded_at}")

if __name__ == "__main__":
    action = input("Enter 'generate' to generate data or 'clear' to clear the data: ").strip().lower()
    if action == 'generate':
        generate_weather_data()
    elif action == 'clear':
        clear_weather_data()
    else:
        print("Invalid action.")
