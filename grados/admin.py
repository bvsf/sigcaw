from django.contrib import admin
from grados.models import (
    Rango,
    Escalafon,
    Grados
)


@admin.register(Rango)
class RangoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'nombre',
                'color',
                )
        }),
    )
    list_display = (
        'nombre',
        'color',
    )
    search_fields = (
        'nombre',
        'color',
    )


@admin.register(Escalafon)
class EscalafonAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'nombre',
                'rango',
                )
        }),
    )
    list_display = (
        'nombre',
        'rango',
    )
    search_field = (
        'nombre',
        'rango',
    )


@admin.register(Grados)
class GradosAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'nombre',
                'grado_superior',
                'escalafon',
                )
        }),
    )
    list_display = (
        'nombre',
        'grado_superior',
        'escalafon',
    )
    search_fields = (
        'nombre',
        'escalafon',
    )
