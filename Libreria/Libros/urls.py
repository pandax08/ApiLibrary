from django.urls import path,include
from Libros import views 

urlpatterns=[

    path('get-libros/',views.CreateLibros.as_view()),
    path('librofile/',views.FileLibroView.as_view()),
    path('portadalibro/',views.PortadaLibroView.as_view()),
    path('list-libros/',views.ListLibros.as_view()),
    path('delete-libros/',views.DeleteLibro.as_view()),
    path('delete-filelibro/',views.DeleteFileLibro.as_view()),
    path('list-tag-libros/',views.ListTagsLibro.as_view()),
    path('libro-update/',views.UpdateLibro.as_view()),
    path('libro-tag/',views.ListLibrosByTag.as_view()),




]