from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from registration.models import CustomUser
from registration.serializers.register import RegistrationSerilaizer

class RegisterView(APIView):
    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = RegistrationSerilaizer(users, many=True)
        return Response(serializer.data)
		
    def post(self, request, format=None):
        serializer = RegistrationSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
