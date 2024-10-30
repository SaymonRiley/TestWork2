from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ReferralCode, Referral

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ReferralCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCode
        fields = ('code', 'expiration_date', 'created_at')

class ReferralSerializer(serializers.ModelSerializer):
    referred_user = UserSerializer()

    class Meta:
        model = Referral
        fields = ('referred_user', 'referred_at')
