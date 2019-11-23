from django.contrib import admin

from .models import Persona


class PersonaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Persona, PersonaAdmin)


from .models import Proyectos


class ProyectosAdmin(admin.ModelAdmin):
    pass


admin.site.register(Proyectos, ProyectosAdmin)


from .models import indicadores


class indicadoresAdmin(admin.ModelAdmin):
    pass


admin.site.register(indicadores, indicadoresAdmin)


from .models import costos_fijos


class costos_fijos(admin.ModelAdmin):
    pass


admin.site.register(costos_fijos, costos_fijosAdmin)


from .models import costos_variables


class costos_variablesAdmin(admin.ModelAdmin):
    pass


admin.site.register(costos_variables, costos_variablesAdmin)

from .models import costos_directos

class costos_directos(admin.ModelAdmin):
    pass


admin.site.register(costos_directos, costos_directosAdmin)


from .models import costos_indirectos


class costos_indirectos(admin.ModelAdmin):
    pass

admin.site.register(costos_indirectos, costos_indirectosAdmin)


from .models import Costeos


class Costeos(admin.ModelAdmin):
    pass

admin.site.register(Costeos, CosteosAdmin)


from .models import Zona_geo


class Zona_geo(admin.ModelAdmin):
    pass

admin.site.register(Zona_geo, Zona_geoAdmin)


from .models import region


class region(admin.ModelAdmin):
    pass

admin.site.register(region, regionAdmin)


from .models import municipios


class municipios(admin.ModelAdmin):
    pass

admin.site.register(municipios, municipiosAdmin)


from .models import stk_holder


class stk_holder(admin.ModelAdmin):
    pass

admin.site.register(stk_holder, stk_holderAdmin)


from .models import acciones_stkholder

class acciones_stkholder(admin.ModelAdmin):
    pass

admin.site.register(acciones_stkholder, acciones_stkholderAdmin)
