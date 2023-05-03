from rest_framework.serializers import ModelSerializer
from callbook.models import CategoryModel,CityModel, UserInfoModel



class Categoryserializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'
        
        
class Cityserializer(ModelSerializer):
    class Meta:
        model = CityModel
        fields = '__all__'
        
        
class UserInfoserializer(ModelSerializer):
    class Meta:
        model =  UserInfoModel
        fields = '__all__'                