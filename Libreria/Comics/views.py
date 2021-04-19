from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Comics.models import  Comics,Tomos,Tag,Portada
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ComicsSerializers,TagSerializers
import json
from django.core import serializers
from django.http import JsonResponse
from rest_framework.filters import SearchFilter,OrderingFilter
import os 

class FileView(APIView):
 
  parser_classes = (MultiPartParser, FormParser)
  
  
  def post(self, request, *args, **kwargs):
      
      
      t_id=request.data['id']
      comic=Comics.objects.get(id=t_id)
      comicfile=request.FILES.getlist('comic')
      
      for c in comicfile:
          files=Tomos.objects.create(comicfile=c, comic=comic)
          files.save()
      
      return Response({'message':"Archivo del comic guardado satisfactoriamente"})


class PortadaView(APIView):

  parser_classes = (MultiPartParser, FormParser)
  
  def put(self, request, *args, **kwargs):
      
      portada=Portada.objects.last()
      portada.portada=request.data['portada']
      portada.save()
      
      return Response({'message':"portada guardada satisfactoriamente"})


class ListComics(ListAPIView):
    """permission_classes =[IsAuthenticated]"""

    queryset=Comics.objects.all()
    serializer_class=ComicsSerializers
    filter_backends =  (SearchFilter,OrderingFilter)
    search_fields =('id','titulo','autor','editorial')



class ListComicsByTag(ListAPIView):
    """permission_classes =[IsAuthenticated]"""

    queryset=Comics.objects.all()
    serializer_class=ComicsSerializers
    filter_backends =  (SearchFilter,OrderingFilter)
    search_fields =('id','tags__nombre')    

class CreateComics(APIView):
    
    def post(self,request):
        comic=Comics.objects.create(autor=request.data['autor'],editorial=request.data['editorial'],titulo=request.data['titulo'],descripcion=request.data['descripcion'])
        comic.save()
        tags=request.data['tags']
        
        for i in tags:
            tg=Tag.objects.get(nombre=i)
            comic.tags.add(tg.id)
        return Response({'message':'El libro fue guardado y asignado a un tag satisfactoriamente','id':comic.id})

        
class DeleteComic(APIView):
    def post(self, request):
        id_comic=request.data['id_comic']
        comic=Comics.objects.get(id=id_comic)
        tomos=Tomos.objects.filter(comic=id_comic)
        portada=Portada.objects.get(comic=id_comic)
        for t in tomos:
            os.remove('.'+str(t.comicfile.url))
        tomos.delete()
        os.remove('.'+str(portada.portada.url))
        portada.delete()
        comic.delete()
        return Response({'message':"Comic y archivos eliminados satisfactoriamente"})


class DeleteTomo(APIView):
    def post(self,request):
        
        id_tomo=request.data['id_tomo']
        tomos=Tomos.objects.get(id=id_tomo)
        os.remove('.'+str(tomos.comicfile.url))
        tomos.delete()
        return Response({'message':'Tomo eliminado satisfactoriamente'})


class ListTags(ListAPIView):
    
    queryset=Tag.objects.all()
    serializer_class=TagSerializers
    filter_backends =  (SearchFilter,OrderingFilter)
    search_fields =('id','nombre')



class UpdateComic(APIView):
    def put(self,request):
        
        id_comic=request.data['id_comic']

        comic=Comics.objects.get(id=id_comic)
        if request.data['titulo']:
            comic.titulo=request.data['titulo']
        if request.data['autor']:
            comic.autor=request.data['autor']
        if request.data['editorial']:
            comic.editorial=request.data['editorial']
        if request.data['tags']:
            tags=comic.tags.all()
            for i in request.data['tags']:
                for c in tags:
                    if  i!=c.nombre:
                        tg=Tag.objects.get(nombre=i)
                        comic.tags.add(tg.id)
                 
                
            
        if request.data['descripcion']:
            comic.descripcion=request.data['descripcion']
        comic.save()
        return Response({'message':"Comic actualizado satisfactoriamente"})  
          

