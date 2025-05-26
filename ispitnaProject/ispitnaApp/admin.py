from django.contrib import admin
from .models import *


# Register your models here.

class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)

    def has_add_permission(self, request):
        return request.user.is_superuser


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', "price")

    def has_add_permission(self, request):
        return request.user.is_superuser


class RealEstateAgentAdmin(admin.TabularInline):
    model = RealEstateAgent
    extra = 0


class RealEstateCharacteristicAdmin(admin.TabularInline):
    model = RealEstateCharacteristic
    extra = 1


class RealEstateAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'description',)
    exclude = ("characteristic",)

    inlines = [RealEstateAgentAdmin, RealEstateCharacteristicAdmin]

    def has_add_permission(self, request):
        return Agent.objects.filter(id=request.user.id).exists()

    def save_model(self, request, obj, form, change):
        super(RealEstateAdmin, self).save_model(request, obj, form, change)
        if not change:
            RealEstateAgent.objects.create(real_estate=obj, agent=Agent.objects.filter(user=request.user).first())

    def has_delete_permission(self, request, obj=None):
        return not RealEstateCharacteristic.objects.filter(real_estate=obj).exists()

    def has_change_permission(self, request, obj=None):
        return RealEstateAgent.objects.filter(real_estate=obj, agent__user=request.user).exists()


admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Characteristic, CharacterAdmin)
