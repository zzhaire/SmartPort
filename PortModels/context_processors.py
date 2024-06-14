
def user_info(request):
    return {
        'user_id': request.session.get('user_id'),
    }
