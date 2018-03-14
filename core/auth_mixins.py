"""
These two decorators are required because the standard authorization libraries
like django-braces do not work (supposedly because of incompatible api)
- standard api has user.is_authenticated() method
- channel api has boolean property user.is_authenticated
"""

from django.conf import settings
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def channel_login_required(func):
    def wrapper(self, *args, **kwargs):
        user = self.scope['user']
        if user.is_authenticated:
            return func(self, *args, **kwargs)

        else:
            raise PermissionDenied()
    return wrapper


class LoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)

        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)
