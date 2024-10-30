

from django.contrib import admin
from .models import *

@admin.register(ReferralCode) 
class ReferralCodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'expiration_date')  
    search_fields = ('code',)  

admin.site.register(Referral)

