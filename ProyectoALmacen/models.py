from django.db import models
# Create your models here.
# Al aplicar esta herencia, Django va a saber que Author es una tabla en la BD



class classroom (models.Model):
    clase=models.CharField (verbose_name='clase', # etiqueta dentro de la tabla
    max_length= 100,
    default=''
    )
    entrytime=models.DateTimeField (verbose_name='hora de entrada',
    default='')
    departuretime=models.DateTimeField (verbose_name='hora de salida',
    default='')
    sites=models.PositiveSmallIntegerField (verbose_name='sites',
    max_length= 60,)
    class Meta:
        verbose_name_plural='Clases'

    def __str__(self):
        return self.clase

class teachers (models.Model):
    Nombre=models.CharField (verbose_name='nombre', # etiqueta dentro de la tabla
    max_length= 100,
    default=''
    )
    contrasena=models.CharField(verbose_name='Contraseña',
    max_length=100,
    default='',
    db_column='contraseña')
    classrooms=models.ManyToManyField(classroom)
    asignature=models.CharField(verbose_name='asignatura',)
    class Meta:
        verbose_name_plural='Profesores'
        def __str__(self):
            return self.title

class fathers (models.Model):
    name=models.CharField (verbose_name='Nombre', # etiqueta dentro de la tabla
    max_length= 100,
    default=''
    )
    last_name=models.CharField(verbose_name='Apellido',
    max_length=150,
    default='')
    age=models.DateField (verbose_name='Fecha de Nacimiento',
    default='')
    number=models.PositiveSmallIntegerField (verbose_name='Teléfono',
    max_length=12 )
    class Meta:
        verbose_name_plural='Padres'

    def __str__(self):
        return f"{self.name} {self.last_name}"


class childs (models.Model):
    name=models.CharField (verbose_name='Nombre', # etiqueta dentro de la tabla
    max_length= 100,
    default=''
    )
    last_name=models.CharField (verbose_name='Apellido',
    max_length=150,
    default='')
    age=models.DateField (verbose_name='Fecha de Nacimiento',
    default='0000/00/00 00:00')
    average=models.PositiveSmallIntegerField (verbose_name='Nota Media',
    default=0)
    father=models.ManyToManyField(fathers)
    school=models.ManyToManyField(classroom)
    class Meta:
        verbose_name_plural='Niños'

    def __str__(self):
        return f"{self.name} {self.last_name}"