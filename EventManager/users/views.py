# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            'detail': 'user successful created',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    
class LogoutView(APIView):
    authentication_classes = []
    permission_classes = [] 

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"refresh": "This field is required."}, status=400)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "loged out successfully"}, status=200)
        except Exception:
            return Response({"detail": "unavaileble token"}, status=400)

