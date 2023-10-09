from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import  *# importar los formularios 

#login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
    
        else:
            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})

# Vista de registro
def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"AppCoder/registro.html" ,  {"form":form})


# html para ver paginas. 

def inicio(request):
    return render(request,"AppCoder/inicio.html" )



#para ver a los usuarios de la BD en la pagina de usuarios
@login_required
def ver_usuario(request):

    todos = Usuario.objects.all() #accedo a los usuarios de la BD
    return render(request,"AppCoder/usuarios.html", {"todos_usuarios":todos}) #envío al usuario.html el diccionario todos_usuarios

def ver_galeria(request):
    return render(request,"AppCoder/galeria-imagenes.html" ) 

def ver_tour(request):
    return render(request,"AppCoder/tour.html" ) 

def ver_camara(request):
    return render(request,"AppCoder/camaras.html" )

def ver_tripode(request):
    return render(request,"AppCoder/tripodes.html" )

def ver_telescopio(request):
    return render(request,"AppCoder/telescopios.html" )

def ver_montura(request):
    return render(request,"AppCoder/monturas.html" )

def ver_binoculares(request):
    return render(request,"AppCoder/binoculares.html" )


#Vistas para crear formularios

#USUARIO-------------------------------
def crear_usuario(request):
    if request.method == "POST": #hacemos click al boton enviar / informacion del boton
        miFormulario = Usuario_Form(request.POST) #aqui llega y guarda info del html
        
        if miFormulario.is_valid(): #si la info es valida
            info = miFormulario.cleaned_data # la informacion la convierte en un diccionario info
            usuario_nuevo = Usuario(nombre=info["nombre"], 
                                    edad=info["edad"], #se crea un nuevo usuario con el model usuario, se envían los parametros de la class Usuario(
                                                                    correo=info["correo"], 
                                    direccion=info["direccion"])        
            usuario_nuevo.save() #se guarde el nuevo usuario
            return render(request, "AppCoder/inicio.html")
    else: #si no hacemos click al enviar
        miFormulario = Usuario_Form() #se muestra formulario vacio

        # el objeto mi formulario de la class Usuario_Form, lo paso al html
        return render (request, "AppCoder/crear-usuario.html", {"form": miFormulario}) #contexto para enviar info al html

#FOTOGRAFIA-------------------------------------
def crear_fotografia(request):
    if request.method == "POST": 
        miFormulario = Fotografia_Form(request.POST)
        
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            foto_nueva = Fotografia(imagen=info["imagen"],
                                    autor=info["autor"],
                                    lugar=info["lugar"],
                                    camara=info["camara"], 
                                    objetivo=info["objetivo"], 
                                    fecha=info["fecha"], 
                                    iso=info["iso"],  
                                    diafragma_f=info["diafragma_f"])  
            foto_nueva.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = Fotografia_Form() 
        return render (request, "AppCoder/crear-imagen.html", {"form_foto": miFormulario})

#RESERVAR TOUR-------------------------------------
def reservar_tour(request):
    if request.method == "POST": 
        miFormulario = Reservar_tour_Fomr(request.POST)
        
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            reserva_nueva = Tour(nombre=info["nombre"],
                                            total_adultos=info["total_adultos"],
                                            total_ninios=info["total_ninios"],
                                            fecha_reserva=info["fecha_reserva"],
                                            fecha_tour=info["fecha_tour"],
                                            tipo_tour=info["tipo_tour"],)  
            reserva_nueva.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = Reservar_tour_Fomr() 
        return render (request, "AppCoder/reservar-tour.html", {"form_reserva": miFormulario})

# Crear Cámara------------------------------------
def crear_camara(request):
    if request.method == "POST": 
        miFormulario = Camara_Form(request.POST)
        
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            camara_nueva = Camara(tipo=info["tipo"],
                                  marca=info["marca"],
                                  precio=info["precio"],
                                  color=info["color"])
                                  
            camara_nueva.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = Camara_Form() 
        return render (request, "AppCoder/crear-camara.html", {"form_crear_camara": miFormulario})

# Crear Tripode------------------------------------
def crear_tripode(request):
    if request.method == "POST": 
        miFormulario = Tripode_Form(request.POST)
        
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            tripode_nuevo = Tripode(marca=info["marca"],
                                  precio=info["precio"],)
                                  
            tripode_nuevo.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = Tripode_Form() 
        return render (request, "AppCoder/crear-tripode.html", {"form_crear_tripode": miFormulario})

# Crear telescopio------------------------------------------------------------
def crear_telescopio(request):
    if request.method == "POST": 
        miFormulario = Telescopio_Form(request.POST)
        
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            telescopio_nuevo = Telescopio(tipo=info["tipo"],
                                        apertura=info["apertura"],
                                        df=info["df"],
                                        f=info["f"],
                                        marca=info["marca"])
                                  
            telescopio_nuevo.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = Telescopio_Form() 
        return render (request, "AppCoder/crear-telescopio.html", {"form_crear_telescopio": miFormulario})
    
#Crear Montura-----------------------------------------------------
def crear_montura(request):
    if request.method == "POST": 
        miFormulario = Montura_Form(request.POST)
        
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            montura_nueva = Montura(tipo=info["tipo"],
                                    seguimiento=info["seguimiento"],
                                    carga_max=info["carga_max"],
                                    marca=info["marca"],
                                    peso=info["peso"])
                                  
            montura_nueva.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = Montura_Form() 
        return render (request, "AppCoder/crear-montura.html", {"form_crear_montura": miFormulario})
    
#Crear Binocular.--------------------------------------------
def crear_binocular(request):
    if request.method == "POST": 
        miFormulario = Binocular_Form(request.POST)
        
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            binocular_nuevo = Binocular(marca=info["marca"],
                                        apertura=info["apertura"],
                                        aumentos=info["aumentos"],
                                        peso=info["peso"])
                                  
            binocular_nuevo.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = Binocular_Form() 
        return render (request, "AppCoder/crear-binocular.html", {"form_crear_binocular": miFormulario})
    
# FORMULARIO PARA BUSCAR USUARIO

def buscar_usuario (request):

    return render(request, "AppCoder/buscar-usuario.html")

def resultado_usuario(request):

    if request.GET["nombre"]: #el nombre que gurada al hacer click boton buscar
        nombre = request.GET["nombre"] #nombre ingresado, lo guardo en la variable nombre
        usuario_resultado = Usuario.objects.filter(nombre__icontains=nombre) #__iexact (resultado exacto)//__icontains (si contiene) filtrar en todos los objetos de la clase Usuario// __incontain, si los modelos de usuario contiene nombre buscado
    
        return render(request, "AppCoder/resultado-usuario.html", {"valor":nombre, "res": usuario_resultado})

    return render(request, "AppCoder/resultado-usuario.html")

# VISTAS PARA ELIMINAR --------------------------------------------------------------

#Eliminar usuario

def eliminar_usuario(request, usuario_nombre): #envío nombre usuario que borraré
    usuario_escogido = Usuario.objects.get(nombre = usuario_nombre) #usuario escogido es el nombre de la BD
    usuario_escogido.delete() #borro usuario
    todos = Usuario.objects.all() #accedo a los usuarios de la BD actualizada sin usuario escogido
    return render(request,"AppCoder/usuarios.html", {"todos_usuarios":todos}) #contexto la nueva BD
# ahora hay que complementar el url usuarios.html y crear un url

#falta una vista para actualizar!!!!!!!!!!!!!!!!!

# clase 23 Vista con Class
