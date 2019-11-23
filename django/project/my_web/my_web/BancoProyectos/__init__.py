class Banco_de_Proyectos (models.Models):
        nombre_proyecto = models.Charfield(max_length=200, null=False, blank=False)
        objetivo= models.Charfield(max_lenght=200, null=False, blank=False)
        indicadores=models.ManyToManyField('Linea_Base','Meta', null=False, blank=False)
        zona_geo= models.ManyToManyField('Region','Municipio','Localidad',null=False, blank=False)
        stk_holder= models.ManyToManyField('Agente_Involucrado','Nivel_interes','Nivel_influencia','Acciones','Estrategias',null=False, blank=False)
        costeos= models.ManyToManyField('Costeos', null=False, )
        duracion_inicio = models.DateTimeField('Fecha_de_Inicio', null=False, blank=False)
        duracion_fin = models.DateTimeField('Fecha_de_Finalizacion', null=False, blank=False)

class Costeo (models.Models):
        costos_fijos= models.ManyToManyField('Costos_Fijos', null=False, blank=False)
        costos_variables= models.ManyToManyField('Costos_Variables')
        costos_directos= models.ManyToManyField('Costos_Directos')
        costos_indirectos= models.ManyToManyField('Costos_Indirectos')


       #Agregar Tabla de costeo por mes y CurvaS



