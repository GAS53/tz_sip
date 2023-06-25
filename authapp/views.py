from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from authapp.serializers import UserSerializer, LoginSerializer
from baseapp.models import CustomUser

class CreaterUserAPI(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        serialzer = UserSerializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        CustomUser.objects.create_user(serialzer.data)
        user = CustomUser.objects.get_by_natural_key(serialzer.data['username'])
        refresh = RefreshToken.for_user(user)
        res = {"user": serialzer.data, "refresh": str(refresh), "access": str(refresh.access_token),}
        return Response(res, status=status.HTTP_201_CREATED)


class LoginViewAPI(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RefreshTokenAPI(generics.CreateAPIView, TokenRefreshView):
    permission_classes = (AllowAny,)


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)