from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.



class Libros(models.Model):
    
    autor=models.CharField(max_length=30)
    editorial=models.CharField(max_length=30)
    titulo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=500)
    tags=models.ManyToManyField('TagLibro')

    def __str__(self):
        return self.titulo


class TagLibro(models.Model):
    nombre=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre



class Libro(models.Model):
    librofile=models.FileField(upload_to='libros_files/files', null=True)
    libro=models.ForeignKey('Libros',on_delete=models.CASCADE,related_name='libros')
    def __str__(self):
        return self.libros.titulo



class PortadaLibro(models.Model):
    libro=models.OneToOneField(Libros,on_delete=models.CASCADE)
    portadalibro=models.FileField(upload_to='libros_files/portadas', null=True)
    def __str__(self):
        return self.libros.titulo



@receiver(post_save, sender=Libros)
def crear_file_libro(sender, instance, created, **kwargs):
    if created:
        
        PortadaLibro.objects.create(libro=instance)