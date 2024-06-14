# middleware.py
from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 定义不需要登录的路径
        exempt_urls = ['/login/', '/register/']

        # 检查用户是否已登录且访问的路径不是豁免路径
        if not request.session.get('user_id') and request.path not in exempt_urls:
            return redirect('/login/')

        response = self.get_response(request)
        return response
