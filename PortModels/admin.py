from django.contrib import admin
from .models import Weather,Ship, Berth, Service, OceanCurrent,RecordBerth,RecordServer

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('weather_id', 'recorded_at', 'warning_level', 'description','temperature','rainfall')
    search_fields = ('weather_id', 'recorded_at', 'warning_level')
    list_filter = ('warning_level', 'recorded_at')


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ('ship_id', 'type', 'contact_info', 'draft_depth', 'login_status')
    search_fields = ('ship_id', 'type')
    list_filter = ('type', 'login_status')


@admin.register(Berth)
class BerthAdmin(admin.ModelAdmin):
    list_display = ('berth_id', 'status', 'area')
    search_fields = ('berth_id', 'area')
    list_filter = ('area', 'status')


@admin.register(OceanCurrent)
class OceanCurrentAdmin(admin.ModelAdmin):
    list_display = ('ocean_current_id', 'recorded_at', 'silt_condition', 'depth')
    search_fields = ('ocean_current_id', 'recorded_at')
    list_filter = ('silt_condition',)

# @admin.RecordBerth(RecordBerth)
# class RecordBerthAdmin(admin.ModelAdmin):
#     list_display = ('ocean_current_id', 'recorded_at', 'silt_condition', 'depth')
#     pass