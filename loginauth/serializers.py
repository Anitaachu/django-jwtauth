from django.contrib.auth.models import User
from rest_framework import serializers, validators




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'username', 'email','password')
        extra_kwargs = {
            'password' : {'write_only': True},
            'email': {'required': True, 
            'validators':[validators.UniqueValidator(User.objects.all(), "A user with that email already exist")]

        }
        }

        def create(self, validated_data):
            password = validated_data.pop("password")
            user = User(**validated_data)
            user.set_password(password)
            user.save()

            return user





