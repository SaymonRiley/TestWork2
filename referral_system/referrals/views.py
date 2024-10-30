from django.contrib.auth.models import User
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import ReferralCode, Referral
from .serializers import UserSerializer, ReferralCodeSerializer, ReferralSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import timedelta
import random, string


def generate_unique_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

class CreateReferralCodeView(generics.CreateAPIView):
    serializer_class = ReferralCodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if hasattr(request.user, 'referral_code'):
            return Response({"detail": "У вас уже есть активный реферальный код."}, status=status.HTTP_400_BAD_REQUEST)

        code = generate_unique_code()
        expiration_date = timezone.now() + timedelta(days=30)
        ReferralCode.objects.create(user=request.user, code=code, expiration_date=expiration_date)
        
        return Response({"code": code, "expiration_date": expiration_date}, status=status.HTTP_201_CREATED)

class DeleteReferralCodeView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        if not hasattr(request.user, 'referral_code'):
            return Response({"detail": "У вас нет активного реферального кода."}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.referral_code.delete()
        return Response({"detail": "Реферальный код удалён."}, status=status.HTTP_204_NO_CONTENT)

class RegisterByReferralCodeView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        referral_code = request.data.get('referral_code')
        if not ReferralCode.objects.filter(code=referral_code, expiration_date__gt=timezone.now()).exists():
            return Response({"detail": "Неверный или истекший реферальный код."}, status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.create_user(username=username, password=password)
        
  
        referrer = ReferralCode.objects.get(code=referral_code).user
        Referral.objects.create(referrer=referrer, referred_user=user)
        
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

class ListReferralsView(generics.ListAPIView):
    serializer_class = ReferralSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Referral.objects.filter(referrer=self.request.user)
