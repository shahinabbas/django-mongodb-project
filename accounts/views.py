from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import (PersonSerializer)
from .db_connections import db

class SignupView(generics.CreateAPIView):
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            new_person = {
                'username': data['username'],
                'email': data['email'],
                'password': data['password']  # Note: You should hash the password before saving it
            }
            db['Person'].insert_one(new_person)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
