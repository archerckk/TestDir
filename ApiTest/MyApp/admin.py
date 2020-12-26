from django.contrib import admin

# Register your models here.
from MyApp.models import *

admin.site.register(DB_diss)#注册函数，里面写类型名，不是类本身，不用加（）
admin.site.register(DB_home_href)
admin.site.register(DB_project)