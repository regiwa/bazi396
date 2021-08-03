from django.contrib import admin
from .models import UserPersona, UserProfile, UserInterest, bz_persona, bz_langit, bz_kua, bz_arti, bz_bumi, bz_story, bz_annual, bz_health

# Register your models here.
admin.site.register(UserPersona)
admin.site.register(UserProfile)
admin.site.register(UserInterest)
admin.site.register(bz_persona)
admin.site.register(bz_arti)
admin.site.register(bz_story)
admin.site.register(bz_health)
admin.site.register(bz_kua)
admin.site.register(bz_annual)
admin.site.register(bz_langit)
admin.site.register(bz_bumi)
