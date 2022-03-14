from django.contrib.admin import site, ModelAdmin
from .models import Participant, Interview

class ProfileAdmin(ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

site.register(Participant, ProfileAdmin)
site.register(Interview, ProfileAdmin)