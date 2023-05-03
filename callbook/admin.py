from django.contrib import admin

from .models import CategoryModel, CityModel ,UserInfoModel


admin.site.register(CategoryModel)
admin.site.register(CityModel)
admin.site.register(UserInfoModel)