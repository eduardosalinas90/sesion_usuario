from django.contrib import admin
from .models import Registrado
from .forms import RegistroForm

# Register your models here.
class AdminRegistrado(admin.ModelAdmin):

    list_display  = ["email", "nombre","timestamp"]
    form          = RegistroForm
    list_filter   = ["timestamp"]
    list_editable = ["nombre"]
    search_fields = ["nombre","email"]
    # class Meta:
    #     model = Registrado

admin.site.register(Registrado,AdminRegistrado)
