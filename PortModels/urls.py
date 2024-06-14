from django.urls import path, re_path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("home/", views.home, name="home"),
    path("info/change/", views.info_change, name="info_charge"),
    path("info/show/", views.info_show, name="info_show"),
    path("user_info/", views.user_info, name="user_info"),
    path("info/update_pwd/", views.update_pwd, name="update_pwd"),
    path("weather/", views.weather_table, name="weather_table"),
    path("current/", views.current_table, name="current_table"),
    path("server/", views.server_table, name="server_table"),
    path("my_list/", views.my_list, name="my_list"),
    path("get_list/", views.get_list, name="get_list"),
    path("test/", views.test, name="test"),
    path("test_get/", views.test_get, name="test_get"),
    path("api/berths/", views.get_berths, name="get_berths"),
    path("api/occupy_berth/", views.occupy_berth, name="occupy_berth"),
    path("api/leave_berth/", views.leave_berth, name="leave_berth"),
    path("api/user_records/", views.get_records, name="get_records"),
    path("records/", views.get_user_records, name="get_user_records"),
    # re_path(r"^.*$", views.notFind, name="404"),
]
