from rest_framework import serializers 
from Comics.models import Comics,Tomos,Portada,Tag


class TomosSerializers(serializers.ModelSerializer):
    
    
    class Meta():
        model=Tomos
        fields=['id','comicfile']   


class PortadaSerializers(serializers.ModelSerializer):

    class Meta():
        model=Portada
        fields=['id','portada']


class TagSerializers(serializers.ModelSerializer):

    class Meta():
        model=Tag
        fields=['id','nombre']


class ComicsSerializers(serializers.ModelSerializer):
    
    portada=PortadaSerializers(read_only=True)
    tags=TagSerializers(read_only=True,many=True)
    tomos=TomosSerializers(read_only=True,many=True)
    
    class Meta():
        model = Comics

        fields=['id','autor','editorial','titulo','descripcion','tags','portada','tomos']