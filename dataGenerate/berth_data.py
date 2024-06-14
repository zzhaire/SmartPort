import os
import sys
import django

# 设置 Django 环境
# 确保项目目录在 sys.path 中
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SmartPort.settings')
django.setup()

from PortModels.models import Berth

def clear_berth_data():
    Berth.objects.all().delete()
    print("Cleared all berth data.")

def generate_berth_data():
    berths = []

    # 生成深水区泊位
    for i in range(1, 24):
        berth_id = f"Dberth{i:02d}"
        berths.append(Berth(berth_id=berth_id, status=False, area="深水区"))

    # 生成浅水区泊位
    for i in range(1, 45):
        berth_id = f"Sberth{i:02d}"
        berths.append(Berth(berth_id=berth_id, status=False, area="浅水区"))

    # 生成中水位泊位
    for i in range(1, 37):
        berth_id = f"Mberth{i:02d}"
        berths.append(Berth(berth_id=berth_id, status=False, area="中水位"))

    # 批量插入泊位数据
    Berth.objects.bulk_create(berths)
    print(f"Generated {len(berths)} berth records.")

if __name__ == "__main__":
    action = input("Enter 'generate' to generate data or 'clear' to clear the data: ").strip().lower()
    if action == 'generate':
        generate_berth_data()
    elif action == 'clear':
        clear_berth_data()
    else:
        print("Invalid action.")
