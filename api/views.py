from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .serializers import CustomTokenObtainPairSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

#class TokenObtainPairViewCustom(TokenObtainPairView):
  #def post(self, request, *args, **kwargs):
      #response = super().post(request, *args, **kwargs)
      #response.data['username'] = self.user.username
      #return response
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.user
        response = super().post(request, *args, **kwargs)
        response.data['username'] = user.username
        return response

class LogoutView(generics.GenericAPIView):
  def post(self, request, *args, **kwargs):
      try:
          refresh_token = request.data['refresh']
          token = RefreshToken(refresh_token)
          token.blacklist()
          return Response(status=status.HTTP_205_RESET_CONTENT)
      except Exception as e:
          return Response(status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  lookup_field = 'username'
