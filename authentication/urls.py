from django.urls import path
from rest_framework.authtoken import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import Logout, UserCreateView, UserListView, UserDeleteView, UserDetailView

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', Logout.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('list/', UserListView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view())
]
