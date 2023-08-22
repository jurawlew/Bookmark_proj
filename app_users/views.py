from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView

from app_users.models import User
from app_users.serializers import RegisterUserSerializer, LoginUserSerializer


class Register(generics.CreateAPIView):
    """ """
    serializer_class = RegisterUserSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post']


class Login(TokenObtainPairView):
    """ """
    queryset = User.objects.all()
    serializer_class = LoginUserSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post']


class Logout(APIView):
    """ """
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post']

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as exc:
            return Response(status=status.HTTP_400_BAD_REQUEST)
