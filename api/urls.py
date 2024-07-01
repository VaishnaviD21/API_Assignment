from django.urls import path
from .views import UserRegisterView, TokenRefreshView, LogoutView, UserDetailView,CustomTokenObtainPairView

urlpatterns = [
  path('register/', UserRegisterView.as_view(), name='register'),
  #path('login/', TokenObtainPairViewCustom.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('user/<str:username>/', UserDetailView.as_view(), name='user_detail'),
  path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]