from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ('id', 'username', 'password', 'email')
      extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
      user = User(
          email=validated_data['email'],
          username=validated_data['username']
      )
      user.set_password(validated_data['password'])
      user.save()
      return user
      
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        return data