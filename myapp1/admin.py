from django.contrib import admin
from .models import UserRegInfo, Operatelog
# Register your models here.
admin.site.register(UserRegInfo)
admin.site.register(Operatelog)