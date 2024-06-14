from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Ship, Weather, OceanCurrent, RecordServer, Berth, RecordBerth
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from datetime import datetime
from django.views.decorators.http import require_http_methods, require_POST
import uuid
from django.utils import timezone


def login(request):
    if request.method == "GET":
        return render(request, "modules/login.html")
    else:
        # 获取 POST 请求中的表单数据
        username = request.POST.get("username")
        password = request.POST.get("password")
        response_data = {
            "message": "登录成功",
            "username": username,
        }

        try:
            user = Ship.objects.get(user_id=username)
            if user.pwd == password:
                user.login_status = True
                user.save()
                request.session["user_id"] = user.user_id
                response_data["redirect_url"] = "/home"
            else:
                response_data["message"] = "登录失败，密码错误"
        except ObjectDoesNotExist:
            response_data["message"] = "登录失败，用户未注册"

        return JsonResponse(response_data)


def logout(request):
    user_id = request.session.get("user_id")
    if user_id:
        try:
            user = Ship.objects.get(user_id=user_id)
            user.login_status = False
            user.save()
            del request.session["user_id"]  # 删除session
            response_data = {
                "message": "登出成功",
            }
        except ObjectDoesNotExist:
            response_data = {
                "message": "登出失败，未找到已登录的用户",
            }
    else:
        response_data = {
            "message": "登出失败，未找到已登录的用户",
        }
    return JsonResponse(response_data)


def register(request):
    if request.method == "GET":
        return render(request, "modules/register.html")
    else:
        # 获取 POST 请求中的表单数据
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")

        response_data = {
            "message": "注册成功，请登录",
            "username": username,
        }

        if password != confirmPassword:
            response_data["message"] = "注册失败，密码和确认密码不一致"
            return JsonResponse(response_data)

        try:
            user = Ship.objects.get(user_id=username)
            if user:
                response_data["message"] = "注册失败，重复的用户名"
                return JsonResponse(response_data)

        except ObjectDoesNotExist:
            new_user = Ship(user_id=username, pwd=password, login_status=False)
            new_user.save()
            response_data["redirect_url"] = "/login"
        return JsonResponse(response_data)


def home(request):
    user_id = request.session.get("user_id", None)
    print(user_id)
    return render(request, "home.html", {"user_id": user_id})


def info_change(request):
    if request.method == "GET":
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("/login/")
        try:
            user = Ship.objects.get(user_id=user_id)
            user_data = {
                "user_id": user.user_id,
                "ship_id": user.ship_id,
                "draft_depth": user.draft_depth,
                "type": user.type,
                "contact_info": user.contact_info,
            }
            # print(user_data)
            return render(
                request,
                "modules/info_table.html",
                {"user_id": user_id, "user_data": user_data},
            )
        except ObjectDoesNotExist:
            return redirect("/login/")
    elif request.method == "POST":
        user_id = request.session.get("user_id")
        if not user_id:
            return JsonResponse({"message": "用户未登录"}, status=400)

        try:
            data = json.loads(request.body.decode("utf-8"))
            user_id = request.session.get("user_id")
            # print("Session user_id:", user_id)
            # print("Received data:", data)  # 打印接收到的数据
            user = Ship.objects.get(user_id=user_id)
            # print("Found user:", user)  # 打印找到的用户
            user.ship_id = data.get("ship_id")
            user.draft_depth = data.get("draft_depth")
            user.type = data.get("type")
            user.contact_info = data.get("contact_info")
            user.save()
            return JsonResponse({"message": "信息更新成功"})
        except ObjectDoesNotExist:
            return JsonResponse({"message": "用户不存在"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"message": "JSON解析错误"}, status=400)


@require_http_methods(["GET"])
def info_show(request):
    return render(request, "modules/info_show.html")


def user_info(request):
    user_id = request.session.get("user_id")
    try:
        ship = Ship.objects.get(user_id=user_id)
        ship_data = {
            "user_id": ship.user_id,
            "ship_id": ship.ship_id,
            "type": ship.type,
            "contact_info": ship.contact_info,
            "draft_depth": ship.draft_depth,
            "login_status": ship.login_status,
            "pwd": ship.pwd,
        }
        return JsonResponse(ship_data)
    except Ship.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)


def update_pwd(request):
    if request.method == "GET":
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("/login/")

        return render(request, "modules/update_pwd.html")

    elif request.method == "POST":
        user_id = request.session.get("user_id")
        print()
        if not user_id:
            return JsonResponse({"success": False, "message": "用户未登录"}, status=400)

        try:
            user = Ship.objects.get(user_id=user_id)
            data = json.loads(request.body)
            current_pwd = data.get("current_pwd")
            new_pwd = data.get("new_pwd")
            confirm_pwd = data.get("confirm_pwd")

            if not current_pwd == user.pwd:
                return JsonResponse(
                    {"success": False, "message": "当前密码错误"}, status=400
                )

            if new_pwd != confirm_pwd:
                return JsonResponse(
                    {"success": False, "message": "新密码和确认密码不一致"}, status=400
                )

            user.pwd = new_pwd
            user.save()

            return JsonResponse({"success": True, "message": "密码修改成功"})

        except ObjectDoesNotExist:
            return JsonResponse({"success": False, "message": "用户不存在"}, status=400)


def weather_table(request):
    weather_data = Weather.objects.all().order_by("-recorded_at")
    # print(weather_data)
    return render(request, "modules/weather_table.html", {"weather_data": weather_data})


def current_table(request):
    ocean_current_data = OceanCurrent.objects.all().order_by("-recorded_at")
    print(ocean_current_data)
    return render(
        request,
        "modules/current_table.html",
        {"ocean_current_data": ocean_current_data},
    )


@csrf_exempt
def server_table(request):
    if request.method == "GET":
        return render(request, "modules/server_table.html")
    else:
        new_record = RecordServer()
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        user_id = request.session.get("user_id")
        if not user_id:
            return JsonResponse({"message": "用户未登录"}, status=400)

        server_details = data.get("description")
        server_info = " ".join(data.get("services"))
        contact_info = data.get("contact_info")
        time = data.get("appointment_time")
        price = data.get("price")

        new_record.record_id = f"record_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        new_record.time = time
        new_record.user_id = user_id
        new_record.server_details = server_details
        new_record.server_info = server_info
        new_record.contact_info = contact_info
        new_record.price = price

        new_record.save()

        return JsonResponse({"message": "提交成功"})


def notFind(request):
    return render(request, "404.html", {}, status=404)


@require_http_methods(["GET"])
def my_list(request):
    return render(request, "modules/my_list.html")


def get_list(request):
    user_id = request.session.get("user_id")
    records = RecordServer.objects.filter(user_id=user_id).order_by("-time")
    records_json = serializers.serialize("json", records)
    print(records[0].record_id)
    return JsonResponse(records_json, safe=False)


def get_berths(request):
    berths = Berth.objects.all()
    berth_list = [
        {"berth_id": berth.berth_id, "area": berth.area, "status": berth.status}
        for berth in berths
    ]
    return JsonResponse(berth_list, safe=False)


@require_POST
@csrf_exempt
def occupy_berth(request):
    user_id = request.session.get("user_id")
    user = Ship.objects.get(user_id=user_id)
    data = json.loads(request.body)
    berth_id = data.get("berth_id")
    if user.ship_id == "Null":
        return JsonResponse({"error": "User has not bound a ship"})

    if not berth_id:
        return JsonResponse({"error": "Invalid data"})

    berth = Berth.objects.get(berth_id=berth_id)
    if berth.status:
        return JsonResponse({"error": "Berth already occupied"})

    berth.status = True
    berth.ship_id = user.ship_id
    berth.save()
    record = RecordBerth(
        record_id=str(uuid.uuid4()),
        user_id=user_id,
        ship_id=user.ship_id,
        berth_id=berth_id,
        in_time=timezone.now(),
        berth_state=True,
    )
    record.save()
    return JsonResponse({"message": "Berth occupied successfully"})


@require_POST
@csrf_exempt
def leave_berth(request):
    try:
        data = json.loads(request.body)
        record_id = data.get("record_id")
        user_id = request.session.get("user_id")

        record = RecordBerth.objects.get(
            record_id=record_id, user_id=user_id, berth_state=True
        )
        record.out_time = timezone.now()
        record.berth_state = False
        record.save()

        berth = Berth.objects.get(berth_id=record.berth_id)
        berth.status = False
        berth.save()

        return JsonResponse({"message": "Berth left successfully"})

    except RecordBerth.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=404)
    except Berth.DoesNotExist:
        return JsonResponse({"error": "Berth not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def get_records(request):
    user_id = request.session.get("user_id")
    records = RecordBerth.objects.filter(user_id=user_id, berth_state=True)
    record_list = [
        {
            "record_id": record.record_id,
            "ship_id": record.ship_id,
            "berth_id": record.berth_id,
            "in_time": record.in_time,
            "berth_state": record.berth_state,
        }
        for record in records
    ]
    return JsonResponse(record_list, safe=False)


@require_http_methods(["GET"])
def get_user_records(request):
    return render(request, "modules/records.html")


@csrf_exempt
def test(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        print(name)
        print(data)
        print(email)
        # 处理数据，例如保存到数据库
        return JsonResponse({"message": "Form submitted successfully!"})
    else:

        return render(
            request,
            "test/test.html",
        )


def test_get(request):
    weather_data = Weather.objects.all().order_by("-recorded_at")
    weather_data_json = serializers.serialize("json", weather_data)
    # print(weather_data)
    return JsonResponse(weather_data_json, safe=False)
