from rest_framework.response import Response
from rest_framework.decorators import api_view
from callbook.models import CityModel,CategoryModel,UserInfoModel
from .serializer import Cityserializer, Categoryserializer, UserInfoserializer

@api_view(['GET'])
def categoryGet(request):
    data = CategoryModel.objects.all()
    serializer = Categoryserializer(data , many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def cityGet(request):
    data = CityModel.objects.all()
    serializer = Cityserializer(data , many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def userinfoGet(request):
    data = UserInfoModel.objects.all()
    serializer = UserInfoserializer(data , many=True)
    
    return Response(serializer.data)



@api_view(['POST'])
def addCategory(request):
    data = request.data
    post = CategoryModel.objects.create(
        name = data['name']
    )
    serializer = Categoryserializer(post,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addCity(request):
    data = request.data
    post = CityModel.objects.create(
        name = data['name']
    )
    serializer = Cityserializer(post,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addUserinfo(request):
    data = request.data
    post = UserInfoModel.objects.create(
        name = data['name'],
        image = request.FILES.get('image'),
        job = data['job'],
        phone = data['phone'],
        email = data['email'],
        note = data ['note'],
        city = CityModel.objects.get(name=data['city']),
        category = CategoryModel.objects.get(name=data['category']),
    )
    serializer = UserInfoserializer(post,many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def updateCategory(request,pk):
    data = request.data 
    post = CategoryModel.objects.get(id=pk)
    serializer = Categoryserializer(post,data=request)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateCity(request,pk):
    data = request.data 
    post = CityModel.objects.get(id=pk)
    serializer = Cityserializer(post,data=request)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
    
@api_view(['PUT'])
def updateUserInfo(request,pk):
    data = request.data 
    post = UserInfoModel.objects.get(id=pk)
    serializer = UserInfoserializer(post,data=request,partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)  



@api_view(['DELETE'])
def deleteCategory(request,pk):
    data = CategoryModel.objects.get(id=pk)
    data.delete()
    return Response('Deleted !!!')

@api_view(['DELETE'])
def deleteCity(request,pk):
    data = CityModel.objects.get(id=pk)
    data.delete()
    return Response('Deleted !!!')

@api_view(['DELETE'])
def deleteUserInfo(request,pk):
    data = UserInfoModel.objects.get(id=pk)
    data.delete()
    return Response('Deleted !!!')

      