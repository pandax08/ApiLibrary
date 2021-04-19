from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Libros.models import  Libros,Libro,TagLibro,PortadaLibro
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import LibrosSerializers,TagLibroSerializers
import json
from django.core import serializers
from django.http import JsonResponse
from rest_framework.filters import SearchFilter,OrderingFilter
import os 

class FileLibroView(APIView):
 
  parser_classes = (MultiPartParser, FormParser)
  
  
  def post(self, request, *args, **kwargs):
      
      
      l_id=request.data['id']
      libro=Libros.objects.get(id=l_id)
      librofile=request.FILES.get('libro')
      file=Libro.objects.create(librofile=librofile, libro=libro)
      file.save()
        
      return Response({'message':"Archivo del libro guardado satisfactoriamente"})


class PortadaLibroView(APIView):

  parser_classes = (MultiPartParser, FormParser)
  
  def put(self, request, *args, **kwargs):
      
      portada_l=PortadaLibro.objects.last()
      portada_l.portadalibro=request.data['portadalibro']
      portada_l.save()
      
      return Response({'message':"portada del libro guardada satisfactoriamente"})


class ListLibros(ListAPIView):
    """permission_classes =[IsAuthenticated]"""

    queryset=Libros.objects.all()
    serializer_class=LibrosSerializers
    filter_backends =  (SearchFilter,OrderingFilter)
    search_fields =('id','titulo','autor','editorial')



class ListLibrosByTag(ListAPIView):
    """permission_classes =[IsAuthenticated]"""

    queryset=Libros.objects.all()
    serializer_class=LibrosSerializers
    filter_backends =  (SearchFilter,OrderingFilter)
    search_fields =('id','tagslibro__nombre')    

class CreateLibros(APIView):
    
    def post(self,request):
        libro=Libros.objects.create(autor=request.data['autor'],editorial=request.data['editorial'],titulo=request.data['titulo'],descripcion=request.data['descripcion'])
        libro.save()
        tags=request.data['tagslibro']
        
        for i in tags:
            tg=TagLibro.objects.get(nombre=i)
            libro.tags.add(tg.id)
        return Response({'message':'El libro fue guardado y asignado a un tag satisfactoriamente','id':libro.id})

        
class DeleteLibro(APIView):
    def post(self, request):
        id_libro=request.data['id_libro']
        libro=Libros.objects.get(id=id_libro)
        file=Libro.objects.get(libro=id_libro)
        portada_l=PortadaLibro.objects.get(libro=id_libro)
        
        os.remove('.'+str(file.librofile.url))
        libro.delete()
        os.remove('.'+str(portada_l.portadalibro.url))
        portada_l.delete()
        libro.delete()
        return Response({'message':"Libros y archivos eliminados satisfactoriamente"})


class DeleteFileLibro(APIView):
    def post(self,request):
        
        id_libro=request.data['id_libro']
        file=Libro.objects.get(id=id_libro)
        os.remove('.'+str(file.librofile.url))
        file.delete()
        return Response({'message':' Archivo del Libro eliminado satisfactoriamente'})


class ListTagsLibro(ListAPIView):
    
    queryset=TagLibro.objects.all()
    serializer_class=TagLibroSerializers
    filter_backends =  (SearchFilter,OrderingFilter)
    search_fields =('id','nombre')



class UpdateLibro(APIView):
    def put(self,request):
        
        id_libro=request.data['id_libro']

        libro=Libros.objects.get(id=id_libro)
        if request.data['titulo']:
            libro.titulo=request.data['titulo']
        if request.data['autor']:
            libro.autor=request.data['autor']
        if request.data['editorial']:
            libro.editorial=request.data['editorial']
        if request.data['tags']:
            tags=libro.tags.all()
            for i in request.data['tags']:
                for c in tags:
                    if  i!=c.nombre:
                        tg=TagLibro.objects.get(nombre=i)
                        libro.tags.add(tg.id)
                 
                
            
        if request.data['descripcion']:
            libro.descripcion=request.data['descripcion']
        libro.save()
        return Response({'message':"Libro actualizado satisfactoriamente"})  
          


