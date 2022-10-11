from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords
# Create your models here.


class Departamento(BaseModel):
    id = models.AutoField(primary_key=True)
    dpto = models.CharField(max_length=50, verbose_name='Departamento')
    state = models.BooleanField('Estado', default=True)


    class Meta:
        db_table = 'departamento'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['id']
    
    def __str__(self):
        return self.dpto




class Distrito(BaseModel):
    id = models.AutoField(primary_key=True)
    dpto = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='id_dpto' )
    distrito = models.CharField(max_length=50, verbose_name='Distrito')
    state = models.BooleanField('Estado', default=True)


    class Meta:
        db_table = 'distrito'
        verbose_name = 'Distrito'
        verbose_name_plural = 'distritos'
        ordering = ['id']
    
    def __str__(self):
        return self.distrito



class Encuesta(BaseModel):

    name = models.CharField(max_length=50, verbose_name='Nombre/s')
    last_name = models.CharField(max_length=50, verbose_name='Apellido/s')
    du = models.CharField(max_length=11, unique=True, blank=False, null=False, verbose_name='N° DNI')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='Departamento' )
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, verbose_name='Distrito' )
    #image = models.ImageField('Imagen Entrevistado', upload_to='entrevistado', blank=True, null=True)
    state = models.BooleanField('Estado', default=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuestas'

    def __srt__(self):
        return self.name


class IndicadorAsistencia(BaseModel):

    asistencia = models.PositiveSmallIntegerField(default=0)
    asistencia_persona = models.ForeignKey(Encuesta, on_delete=models.CASCADE, verbose_name='Indicador de asistencia')

    class Meta:
        db_table = 'asistencia'
        verbose_name = 'Indicador de asistencia'
        verbose_name_plural = 'Indicadores de asistencia'
        ordering = ['id']
    
    def __str__(self):
        return f'Asistencia {self.asistencia_persona} : {self.asistencia}'
