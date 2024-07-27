from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def t1(r):
    return HttpResponse ("<p>this my application</p>")
def t2(r):
    return HttpResponse("<p>hii....</p>")
def t3(y):
    return HttpResponse("<p>hello world....</p>")




from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student
from .serlializers import Std_Serializer

@api_view(['GET'])
def apiview(request):
    api_urls={
          "name":"tamil",
          "contactno":"9087645",
          "email":"tk@gmail.com",
          "address":"kjhsfh"
    }
    return Response(api_urls)

from rest_framework import serializers
from rest_framework import status

@api_view(['POST'])
def api_items(request):
    item=Std_Serializer(data=request.data)
    if student.objects.filter(**request.data).exists():
        raise serializers.ValidationError('this data already exists')
    if item. is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def view_items(request):
    if request.query_params:
        items= student.objects.filter(**request.query_params.dict())
    else:
        items = student.objects.all()

    if items:
        serializer = Std_Serializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_items(request,pk):
    item=student.objects.get(pk=pk)
    data=Std_Serializer(instance=item,data=request.data)
    if data. is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)