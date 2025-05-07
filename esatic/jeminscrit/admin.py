from django.contrib import admin
from .models import Candidat

@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenoms', 'concours_souhaite', 'date_inscription')
    list_filter = ('concours_souhaite', 'date_inscription')
    search_fields = ('nom', 'prenoms', 'email')
    date_hierarchy = 'date_inscription'