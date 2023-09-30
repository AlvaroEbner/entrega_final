from django.urls import path
from AppCoder.views import *



urlpatterns = [
    # urls para ver
    path('', inicio, name= "inicio"),
    path('usuarios/', ver_usuario, name = "usuarios"),
    path('galeria-imagenes/', ver_galeria, name = "galeria-imagenes"),
    path('tour/', ver_tour, name = "tour"),
    path('camaras/', ver_camara, name = "camaras"),
    path('tripodes/', ver_tripode, name = "tripodes"),
    path('telescopios/', ver_telescopio, name = "telescopios"),
    path('monturas/', ver_montura, name = "monturas"),
    path('binoculares/', ver_binoculares, name = "binoculares"),

    #url formularios para crear
    path('crear-usuario/', crear_usuario, name = "crear-usuario"),
    path('crear-imagen/', crear_fotografia, name = "crear-imagen"),
    path('crear-imagen/', crear_fotografia, name = "crear-imagen"),
    path('reservar-tour/', reservar_tour, name = "reservar-tour"),
    path('crear-camara/', crear_camara, name = "crear-camara"),
    path('crear-tripode/', crear_tripode ,name = "crear-tripode"),
    path('crear-telescopio/',crear_telescopio ,name = "crear-telescopio"),
    path('crear-montura/', crear_montura ,name = "crear-montura"),
    path('crear-binocular/', crear_binocular ,name = "crear-binocular"),

    #url formularios busqueda
    path('buscar-usuario/', buscar_usuario ,name = "buscar-usuario"),
    path('resultado-usuario/', resultado_usuario ,name = "resultado-usuario"),

    # url para eliminar 
    path('eliminar-usuario/<usuario_nombre>', eliminar_usuario ,name = "eliminar-usuario"), #agrego el parametro que declaro: def eliminar_usuario(request, usuario_nombre)


]