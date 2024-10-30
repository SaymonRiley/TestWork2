from django.urls import path
from .views import CreateReferralCodeView, DeleteReferralCodeView, RegisterByReferralCodeView, ListReferralsView

urlpatterns = [
    path('create/', CreateReferralCodeView.as_view(), name='create_referral_code'),
    path('delete/', DeleteReferralCodeView.as_view(), name='delete_referral_code'),
    path('register/', RegisterByReferralCodeView.as_view(), name='register_by_referral'),
    path('list/', ListReferralsView.as_view(), name='list_referrals'),
]
