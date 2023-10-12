from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    #login
    path('login', login_request, name="login"), #login de usuario
    path('registro', register, name='registro'), #registro de usuario
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),#logout
    path('editarPerfil', editarPerfil, name="EditarPerfil"), #editar perfil de usuario
    
    # urls para ver
    path('insumos/', ver_insumos, name = "insumos"),
    path('quien-soy/', ver_quien_soy, name = "quien-soy"),
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

    path('buscar-camara/', buscar_camara ,name = "buscar-camara"),
    path('resultado-camara/', resultado_camara ,name = "resultado-camara"),

    path('buscar-tripode/', buscar_tripode ,name = "buscar-tripode"),
    path('resultado-tripode/', resultado_tripode ,name = "resultado-tripode"),

    path('buscar-telescopio/', buscar_telescopio ,name = "buscar-telescopio"),
    path('resultado-telescopio/', resultado_telescopio ,name = "resultado-telescopio"),

    path('buscar-montura/', buscar_montura ,name = "buscar-montura"),
    path('resultado-montura/',resultado_montura ,name = "resultado-montura"),

    path('buscar-binocular/', buscar_binocular ,name = "buscar-binocular"),
    path('resultado-binocular',resultado_binocular ,name = "resultado-binocular"),

    # url para eliminar 
    path('eliminar-usuario/<usuario_nombre>', eliminar_usuario ,name = "eliminar-usuario"), #agrego el parametro que declaro: def eliminar_usuario(request, usuario_nombre)
    path('eliminar-camara/<camara_marca>', eliminar_camara ,name = "eliminar-camara"),
    path('eliminar-tripode/<tripode_marca>', eliminar_tripode,name = "eliminar-tripode"),
    path('eliminar-telescopio/<telescopio_marca>', eliminar_telescopio,name = "eliminar-telescopio"),
    path('eliminar-montura/<montura_marca>', eliminar_montura,name = "eliminar-montura"),
    path('eliminar-binocular/<binocular_marca>', eliminar_binocular,name = "eliminar-binocular"),

]