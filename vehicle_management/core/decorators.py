from django.http import HttpResponseForbidden

def auth_user(user_types=[]):
    def decorator(fun):
        def wrapper(request,*args,**kwargs):
            if request.user.user_type in user_types:
                return fun(request, *args, **kwargs)
            else:
                return HttpResponseForbidden()
        return wrapper
    return decorator