from django.db import models

GENERO_CHOICES = [
    ('M', 'MASCULINO'),
    ('F', 'FEMENINO')
]


ESTUDIOS_CHOICES = [
    ('B','BACHILLERATO'),
    ('L','LICENCIATURA'),
    ('M','MAESTRIA'),
    ('D','DOCTORADO'),
    ('PD','POSTDOCTORADO')
]


OCUPACION_CHOICES = [
    ('ES','ESTUDIANTE'),
    ('EM','EMPLEADO'),
    ('IN','INVESTIGADOR'),
    ('O','OTRO')
]


NIVEL_INTERES = [
    ('B','BAJO'),
    ('M','MEDIO'),
    ('A','ALTO')
]

NIVEL_INFLUENCIA = [
    ('B', 'BAJO'),
    ('M', 'MEDIO'),
    ('A', "ALTO")
]

class Persona(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    apellido_paterno = models.CharField(max_length=200, null=False, blank=False)
    fecha_nacimiento = models.DateTimeField(null=False, blank=False)
    genero = models.CharField(max_length=1, null=False, blank=False, choices=GENERO_CHOICES, default="B")
    nivel_estudios = models.CharField(max_length=2, null=False, blank=False, choices=ESTUDIOS_CHOICES, default="ES")
    ocupacion = models.CharField(max_length=2, null=False, blank=False, choices=OCUPACION_CHOICES)

    #padre= models.ForeignKey('Persona',null=False, blank=False, related_name='hijos_del_padre', on_delete=models.CASCADE)
    #madre= models.ForeignKey('Persona',null=False, blank=False, related_name='hijos_de_la_madre', on_delete=models.CASCADE)
    #hermanos= models.ManyToManyField ('Persona', related_name='mis_hermanos')
    #pareja= models.OneToOneField('Persona', null=False, blank=False, on_delete=models.CASCADE, related_name='mi_pareja')

    def __str__(self):
        return '{},{}'.format(self.nombre, self.apellido_paterno)


class Proyectos(models.Model):
    nombre_proyecto = models.CharField(max_length=200, null=False, blank=False)
    objetivo = models.CharField(max_length=200, null=False, blank=False)
    indicadores = models.ManyToManyField('indicadores')
    zona_geo = models.ManyToManyField('Zona_geo')
    stk_holder = models.ManyToManyField('stk_holder')
    duracion_inicio = models.DateTimeField('Fecha_de_Inicio', null=False, blank=False)
    duracion_fin = models.DateTimeField('Fecha_de_Finalizacion', null=False, blank=False)
    costeos = models.ManyToManyField('Costeos')

class indicadores(models.Model):
    proyecto = models.ForeignKey('Proyectos', on_delete=None , related_name='P_indicadores')
    nombre_indicador = models.CharField(max_length=30)
    linea_base = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=9)
    meta_indicador = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=9)


class costos_fijos(models.Model):
    c_fijos= models.DecimalField(null=False, blank=False, decimal_place=2, max_digits=9)

class costos_variables(models.Model):
    c_variables= models.DecimalField(null=False, blank=False, decimal_place=2, max_digits=9)

class costos_directos(models.Model):
    c_directos= models.DecimalField(null=False, blank=False, decimal_place=2, max_digits=9)

class costos_indirectos(models.Model):
    c_indirectos= models.DecimalField(null=False, blank=False, decimal_place=2, max_digits=9)

class Costeos(models.Model):
    costos_fijos = models.ManyToManyField(costos_fijos, related_name='costos_f')
    costos_variables = models.ManyToManyField(costos_variables, related_name='costos_v')
    costos_directos = models.ManyToManyField(costos_directos, related_name='costos_d')
    costos_indirectos = models.ManyToManyField(costos_indirectos, related_name='costos_i')

class Zona_geo(models.Model):
    regiones= models.ManyToManyField('region')

class region(models.Model):
    nombre = models.CharField(max_length=200)
    municipios = models.ManyToManyField('municipios')

class municipios(models.Model):
    nombre = models.CharField(max_length=200)

class stk_holder(models.Model):
    agente_involucrado= models.CharField(max_length=200)
    nivel_interes= models.CharField(max_length=1, choices=NIVEL_INTERES)
    nivel_influencia = models.CharField(max_length=1, choices=NIVEL_INFLUENCIA)
    acciones_stkholder=models.ManyToManyField('acciones_stkholder')

class acciones_stkholder (models.Model):
    acciones_positivas=models.CharField(max_length=200)
    acciones_negativas = models.CharField(max_length=200)
