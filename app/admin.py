from django.contrib import admin
import reversion

from .models import Houseplant


class HouseplantAdmin(reversion.VersionAdmin):
    list_display = ('common_name', 'created')

admin.site.register(Houseplant, HouseplantAdmin)
