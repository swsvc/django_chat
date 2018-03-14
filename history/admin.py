from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp
from django.contrib import admin

from .models import Room, Message

admin.site.register(Room)
admin.site.register(Message)

admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialApp)

