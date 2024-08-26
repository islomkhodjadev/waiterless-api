from django.urls import path
from .views import RegisterUser, CustomAuthToken, UserView

urlpatterns = [
    # Register new user
    path("register/", RegisterUser.as_view(), name="register-user"),
    # Login and retrieve authentication token
    path("login/", CustomAuthToken.as_view(), name="login-user"),
    # Get the authenticated user's information
    path("user/", UserView.as_view(), name="user-detail"),
    # Update authenticated user's information
    path("user/update/", UserView.as_view(), name="user-update"),
    # Patch authenticated user's information (partial update)
    path("user/patch/", UserView.as_view(), name="user-patch"),
]
