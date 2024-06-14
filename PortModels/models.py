from django.db import models


class Weather(models.Model):
    WEATHER_WARNING_LEVELS = [
        ("normal", "正常"),
        ("alert", "警告"),
        ("danger", "危险"),
    ]

    weather_id = models.CharField(
        max_length=50, primary_key=True, verbose_name="天气编号"
    )
    recorded_at = models.DateTimeField(verbose_name="记录日期时间")
    warning_level = models.CharField(
        max_length=10, choices=WEATHER_WARNING_LEVELS, verbose_name="预警级别"
    )
    description = models.TextField(verbose_name="天气描述")
    temperature = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="气温"
    )
    rainfall = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="降雨量"
    )

    def __str__(self):
        return f"{self.weather_id} - {self.recorded_at}"

    class Meta:
        verbose_name = "天气"
        verbose_name_plural = "天气"


class Ship(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True, verbose_name="用户主键")
    ship_id = models.CharField(max_length=50, verbose_name="船舶编号", default="Null")
    type = models.CharField(max_length=100, verbose_name="船舶类型", default="Null")
    contact_info = models.CharField(
        max_length=255,
        verbose_name="联系方式",
    )
    draft_depth = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="吃水深度", default=0
    )
    login_status = models.BooleanField(default=False, verbose_name="登录状态")
    pwd = models.CharField(default="123456", max_length=20, verbose_name="密码")

    def __str__(self):
        return f"{self.ship_id} - {self.type}"

    class Meta:
        verbose_name = "船舶"
        verbose_name_plural = "船舶"


class Berth(models.Model):
    berth_id = models.CharField(
        max_length=50, primary_key=True, verbose_name="泊位编号"
    )
    status = models.BooleanField(default=False, verbose_name="占用状态")
    area = models.CharField(max_length=50, verbose_name="区域")
    ship_id = models.CharField(
        max_length=50, verbose_name="当前停放船舶", default="未停放"
    )

    def __str__(self):
        return f"{self.berth_id} - {self.area}"

    class Meta:
        verbose_name = "泊位"
        verbose_name_plural = "泊位"


class Service(models.Model):
    service_id = models.CharField(
        max_length=50, primary_key=True, verbose_name="服务编号"
    )
    info = models.CharField(max_length=100, verbose_name="服务描述")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="费用")

    def __str__(self):
        return f"{self.service_id} - {self.type}"

    class Meta:
        verbose_name = "服务"
        verbose_name_plural = "服务"


class OceanCurrent(models.Model):
    ocean_current_id = models.CharField(
        max_length=50, primary_key=True, verbose_name="洋流编号"
    )
    recorded_at = models.DateTimeField(verbose_name="记录日期时间")
    silt_condition = models.CharField(max_length=100, verbose_name="淤沙状态")
    depth = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="深度")

    def __str__(self):
        return f"{self.ocean_current_id} - {self.recorded_at}"

    class Meta:
        verbose_name = "洋流"
        verbose_name_plural = "洋流"


class RecordBerth(models.Model):
    record_id = models.CharField(
        max_length=50, primary_key=True, verbose_name="记录主键"
    )
    user_id = models.CharField(max_length=50, verbose_name="用户主键")
    ship_id = models.CharField(max_length=50, verbose_name="船舶编号", default="Null")
    berth_id = models.CharField(max_length=50, verbose_name="泊位编号")
    in_time = models.DateTimeField(verbose_name="入港时间", null=True, blank=True)
    out_time = models.DateTimeField(verbose_name="离港时间", null=True, blank=True)
    berth_state = models.BooleanField(default=False, verbose_name="当前停放状态")


class RecordServer(models.Model):
    record_id = models.CharField(
        max_length=50, primary_key=True, verbose_name="记录主键"
    )
    time = models.DateTimeField(verbose_name="消费时间")
    user_id = models.CharField(max_length=50, verbose_name="用户主键")
    server_details = models.CharField(
        max_length=100, verbose_name="服务描述", default="无"
    )
    server_info = models.CharField(max_length=50, verbose_name="服务简介", default="无")
    contact_info = models.CharField(max_length=50, verbose_name="联系方式", default="0")
    price = models.DecimalField(
        max_digits=15, decimal_places=2, verbose_name="消费金额"
    )
