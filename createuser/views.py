from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ContactSerializer
from rest_framework.response import Response 
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer


class ContactList(ListCreateAPIView):

    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Contact.objects.filter(username)

class RegisterView(GenericAPIView):
    serializer_class = ContactSerializer
    
    def post(self, request):
        serializer=ContactSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        