from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserSerializer


class RegisterUser(APIView):

    def post(self, request):
        data = request.data

        user = UserSerializer(data=data)
        if user.is_valid(raise_exception=True):
            user = user.save()

            return Response(
                data=UserSerializer(instance=user).data, status=status.HTTP_200_OK
            )


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        if "newToken" in request.data and Token.objects.filter(user=user):
            Token.objects.get(user=user).delete()

        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "phoneNumber": user.phoneNumber.raw_input,
            }
        )


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response(
            data=UserSerializer(instance=request.user).data, status=status.HTTP_200
        )

    def update(self, request):

        user = UserSerializer(instance=request.user, data=request.data)
        if user.is_valid(raise_exception=True):
            user = user.save()

            return Response(
                data=UserSerializer(instance=user).data, status=status.HTTP_200_OK
            )

    def patch(self, request):

        user = UserSerializer(instance=request.user, data=request.data, partial=True)
        if user.is_valid(raise_exception=True):
            user = user.save()

            return Response(
                data=UserSerializer(instance=user).data, status=status.HTTP_200_OK
            )
