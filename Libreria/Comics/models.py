from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.



class Comics(models.Model):
    
    autor=models.CharField(max_length=30)
    editorial=models.CharField(max_length=30)
    titulo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=500)
    tags=models.ManyToManyField('Tag')

    def __str__(self):
        return self.titulo


class Tag(models.Model):
    nombre=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre



class Tomos(models.Model):
    comicfile=models.FileField(upload_to='comics_files/files', null=True)
    comic=models.ForeignKey('Comics',on_delete=models.CASCADE,related_name='tomos')
    def __str__(self):
        return self.comics.titulo



class Portada(models.Model):
    comic=models.OneToOneField(Comics,on_delete=models.CASCADE)
    portada=models.FileField(upload_to='comics_files/portadas', null=True)
    def __str__(self):
        return self.comics.titulo



@receiver(post_save, sender=Comics)
def crear_file_comic(sender, instance, created, **kwargs):
    if created:
        
        Portada.objects.create(comic=instance)