from django.contrib.auth.models import Permission
from .models import Account, Developer
from django.contrib import admin

admin.site.register(Account)
admin.site.register(Developer)
admin.site.register(Permission)
