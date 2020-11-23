from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import PersonSerializer
from .models import Person
from rest_framework import generics
from rest_framework import mixins

# Create your views here.

class PersonViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many = True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    
    def put(self, request, pk = None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, pk=pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk = None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, pk=pk)
        person.delete()
        return Response([])