from django.contrib import admin
from treyler.models.treyler import Treyler


class TreylerAdmin(admin.ModelAdmin):
  list_display = ("title", "treyler_id", "description", "code")



admin.site.register(Treyler, TreylerAdmin)
