from django.contrib import admin
from ProyectoALmacen.models import childs
from ProyectoALmacen.models import fathers
from ProyectoALmacen.models import classroom
from ProyectoALmacen.models import teachers
# Register your models here.

admin.site.register(childs)
admin.site.register(fathers)
admin.site.register(classroom)
admin.site.register(teachers)