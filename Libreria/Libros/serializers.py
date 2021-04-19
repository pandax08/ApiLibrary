from rest_framework import serializers 
from Libros.models import Libros,Libro,PortadaLibro,TagLibro


class LibroSerializers(serializers.ModelSerializer):
    
    
    class Meta():
        model=Libro
        fields=['id','librofile']   


class PortadaLibroSerializers(serializers.ModelSerializer):

    class Meta():
        model=PortadaLibro
        fields=['id','portadalibro']


class TagLibroSerializers(serializers.ModelSerializer):

    class Meta():
        model=TagLibro
        fields=['id','nombre']


class LibrosSerializers(serializers.ModelSerializer):
    
    portadalibro=PortadaLibroSerializers(read_only=True)
    tagslibro=TagLibroSerializers(read_only=True,many=True)
    libro=LibroSerializers(read_only=True,many=True)
    
    class Meta():
        model = Libros

        fields=['id','autor','editorial','titulo','descripcion','tagslibro','portadalibro','libro']