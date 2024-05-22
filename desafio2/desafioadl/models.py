from django.db import models

# Create your models here.
#########################################################################

class Tarea(models.Model):
    descripcion = models.CharField(max_length=255, default="")
    eliminada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ["descripcion"]

class SubTarea(models.Model):
    descripcion = models.CharField(max_length=255)
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Sub Tarea"
        verbose_name_plural = "Sub Tareas"
        ordering = ["descripcion"]
