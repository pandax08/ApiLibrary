from django.urls import path,include
from Comics import views 

urlpatterns=[
    path('get-comics/',views.CreateComics.as_view()),
    path('comicfile/',views.FileView.as_view()),
    path('portada/',views.PortadaView.as_view()),
    path('list-comics/',views.ListComics.as_view()),
    path('delete-comics/',views.DeleteComic.as_view()),
    path('delete-tomo/',views.DeleteTomo.as_view()),
    path('list-tag/',views.ListTags.as_view()),
    path('comic-update/',views.UpdateComic.as_view()),
    path('comic-tag/',views.ListComicsByTag.as_view()),






]