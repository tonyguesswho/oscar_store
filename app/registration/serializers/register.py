from rest_framework import  serializers
from registration.models import CustomUser

class RegistrationSerilaizer(serializers.ModelSerializer):
    """Serilaizers registration request and creates user"""

    password = serializers.CharField(max_length = 128, min_length = 8, write_only = True)


    class Meta:
        model = CustomUser

        fields = ['email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
         return CustomUser.objects.create_user(**validated_data)