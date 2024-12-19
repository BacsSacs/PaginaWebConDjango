from django.contrib import admin
from .models import Project
# Register your models here.

# A continuación vamos a habilitar los campos en modo lectura
# de la fecha de creación y fecha de actualización en el panel 
# de administrador

# este campo es util para mostrarlo en asdata
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

#con la siguiente linea mostramos en el panel de administrador
# el modelo de project
admin.site.register(Project, ProjectAdmin)
