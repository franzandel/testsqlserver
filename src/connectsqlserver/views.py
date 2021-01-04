from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Person
from .serializers import PersonSerializer
from .baseresponse import BaseResponse

@api_view(['GET'])
def peopleView(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return BaseResponse(serializer.data)

@api_view(['GET'])
def personView(request, pk):
    if not Person.objects.filter(id=pk).exists():
        return BaseResponse('Person not found')

    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(person, many=False)
    return BaseResponse(serializer.data)

@api_view(['POST'])
def personCreate(request):
    serializer = PersonSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return BaseResponse(serializer.data)

@api_view(['POST'])
def personUpdate(request, pk):
    if not Person.objects.filter(id=pk).exists():
        return BaseResponse('Person not found')
        
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(instance=person, data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return BaseResponse(serializer.data)
    
@api_view(['DELETE'])
def personDelete(request, pk):
    if not Person.objects.filter(id=pk).exists():
        return BaseResponse('Person not found')

    person = Person.objects.get(id=pk)
    person.delete()
    return BaseResponse('Person successfully deleted')