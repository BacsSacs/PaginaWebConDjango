from django.db import models

# Create your models here.
class Project(models.Model):
    # con verbose_name traducimos a español todas las variables, así en el panel 
    # podemos leer los terminos en nuestro idioma nativo
    title = models.CharField(max_length=200, verbose_name = "Titulo")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edición")

    #con la siguiente clase meta, podemos renombrar los metadatos, en
    # este caso los traduciremos a español
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        # con la siguiente linea vamos a ordenar desde el ultimo dato
        # al más antiguo
        ordering = ["-created"]
    
    # A continuación vamos a mostrar en el panel administrativo
    # el nombre del proyecto
    def __str__(self):
        return self.title