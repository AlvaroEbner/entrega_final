from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import  *# importar los formularios 

#login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from AppCoder.forms import UserRegisterForm, UserEditForm

#avatar-------------------------
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url})

#-------------------------------
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


#Editar usuarios

# Vista de editar el perfil de usuario
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


# Vistas Pagina principal. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def inicio(request):
    return render(request,"AppCoder/inicio.html" )

#Vista para intercambio de insumos
@login_required
def ver_insumos(request):
    return render(request,"AppCoder/insumos.html" )

#no requiere estar iniciar sesión
def ver_quien_soy (request):
    return render(request,"AppCoder/quien-soy.html" )

@login_required
def ver_galeria(request):
    return render(request,"AppCoder/galeria-imagenes.html" ) 



#1)  CRUD ++++++++++++++++++++++++++ VER  +++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def ver_tour(request):
    todos_tour = Tour.objects.all()
    return render(request,"AppCoder/tour.html", {"todos_tour": todos_tour}) 

@login_required
def ver_camara(request):
    todas_camaras =Camara.objects.all()
    return render(request,"AppCoder/camaras.html", {"todas_camaras": todas_camaras}) 

@login_required
def ver_tripode(request):
    todos_tripode =Tripode.objects.all()
    return render(request,"AppCoder/tripodes.html",{"todos_tripode": todos_tripode} )

@login_required
def ver_telescopio(request):
    todos_telescopios = Telescopio.objects.all()
    return render(request,"AppCoder/telescopios.html", {"todos_telescopios":todos_telescopios} )

@login_required
def ver_montura(request):
    todas_monturas = Montura.objects.all()
    return render(request,"AppCoder/monturas.html", {"todas_monturas":todas_monturas} )

@login_required
def ver_binoculares(request):
    todos_binoculares = Binocular.objects.all()
    return render(request,"AppCoder/binoculares.html", {"todos_binoculares":todos_binoculares} )


#no se utiliza
@login_required
def ver_usuario(request):
    todos = Usuario.objects.all() #accedo a los usuarios de la BD
    return render(request,"AppCoder/usuarios.html", {"todos_usuarios":todos}) #envío al usuario.html el diccionario todos_usuarios




#2)  CRUD ++++++++++++++++++++++++++ CREAR +++++++++++++++++++++++++++++++++++++++++++++++++

#USUARIO no se utiliza en la pagina-------------------------------
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
                                #fecha_reserva=info["fecha_reserva"],
                                fecha_tour=info["fecha_tour"],)
                                #tipo_tour=info["tipo_tour"]  
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
                                    goto=info["goto"],
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
    
#3)  CRUD ++++++++++++++++++++++++++ Buscar +++++++++++++++++++++++++++++++++++++++++++++++++++++

def buscar_usuario (request):

    return render(request, "AppCoder/buscar-usuario.html")

def resultado_usuario(request):

    if request.GET["nombre"]: #el nombre que gurada al hacer click boton buscar
        nombre = request.GET["nombre"] #nombre ingresado, lo guardo en la variable nombre
        usuario_resultado = Usuario.objects.filter(nombre__icontains=nombre) #__iexact (resultado exacto)//__icontains (si contiene) filtrar en todos los objetos de la clase Usuario// __incontain, si los modelos de usuario contiene nombre buscado
    
        return render(request, "AppCoder/resultado-usuario.html", {"valor":nombre, "res": usuario_resultado})

    return render(request, "AppCoder/resultado-usuario.html")

#buscar cámara.
def buscar_camara (request):
    return render(request, "AppCoder/buscar-camara.html")

def resultado_camara(request):
    if request.GET["marca"]: #el nombre que gurada al hacer click boton buscar
        marca = request.GET["marca"] #nombre ingresado, lo guardo en la variable nombre
        marca_resultado = Camara.objects.filter(marca__icontains=marca) #__iexact (resultado exacto)//__icontains (si contiene) filtrar en todos los objetos de la clase Usuario// __incontain, si los modelos de usuario contiene nombre buscado
 
        return render(request, "AppCoder/resultado-camara.html", {"valor":marca, "res": marca_resultado})

    return render(request, "AppCoder/resultado-camara.html")

#buscar tripode.
def buscar_tripode (request):
    return render(request, "AppCoder/buscar-tripode.html")

def resultado_tripode(request):
    if request.GET["marca"]: #el nombre que gurada al hacer click boton buscar
        marca = request.GET["marca"] #nombre ingresado, lo guardo en la variable nombre
        marca_resultado = Tripode.objects.filter(marca__icontains=marca) #__iexact (resultado exacto)//__icontains (si contiene) filtrar en todos los objetos de la clase Usuario// __incontain, si los modelos de usuario contiene nombre buscado
 
        return render(request, "AppCoder/resultado-tripode.html", {"valor":marca, "res": marca_resultado})

    return render(request, "AppCoder/resultado-tripode.html")

#buscar telescopio.
def buscar_telescopio (request):
    return render(request, "AppCoder/buscar-telescopio.html")

def resultado_telescopio(request):
    if request.GET["marca"]: #el nombre que gurada al hacer click boton buscar
        marca = request.GET["marca"] #nombre ingresado, lo guardo en la variable nombre
        marca_resultado = Telescopio.objects.filter(marca__icontains=marca) #__iexact (resultado exacto)//__icontains (si contiene) filtrar en todos los objetos de la clase Usuario// __incontain, si los modelos de usuario contiene nombre buscado
 
        return render(request, "AppCoder/resultado-telescopio.html", {"valor":marca, "res": marca_resultado})

    return render(request, "AppCoder/resultado-telescopio.html")

#buscar montura.
def buscar_montura (request):
    return render(request, "AppCoder/buscar-montura.html")

def resultado_montura(request):
    if request.GET["marca"]: #el nombre que gurada al hacer click boton buscar
        marca = request.GET["marca"] #nombre ingresado, lo guardo en la variable nombre
        marca_resultado = Montura.objects.filter(marca__icontains=marca) #__iexact (resultado exacto)//__icontains (si contiene) filtrar en todos los objetos de la clase Usuario// __incontain, si los modelos de usuario contiene nombre buscado
 
        return render(request, "AppCoder/resultado-montura.html", {"valor":marca, "res": marca_resultado})

    return render(request, "AppCoder/resultado-montura.html")

#buscar binocular.
def buscar_binocular (request):
    return render(request, "AppCoder/buscar-binocular.html")

def resultado_binocular(request):
    if request.GET["marca"]: #el nombre que gurada al hacer click boton buscar
        marca = request.GET["marca"] #nombre ingresado, lo guardo en la variable nombre
        marca_resultado = Binocular.objects.filter(marca__icontains=marca) #__iexact (resultado exacto)//__icontains (si contiene) filtrar en todos los objetos de la clase Usuario// __incontain, si los modelos de usuario contiene nombre buscado
 
        return render(request, "AppCoder/resultado-binocular.html", {"valor":marca, "res": marca_resultado})

    return render(request, "AppCoder/resultado-binocular.html")





#4)  CRUD ++++++++++++++++++++++++++ ELIMINAR ++++++++++++++++++++++++++++++++++++

#Eliminar usuario

def eliminar_usuario(request, usuario_nombre): #envío nombre usuario que borraré
    usuario_escogido = Usuario.objects.get(nombre = usuario_nombre) #usuario escogido es el nombre de la BD
    usuario_escogido.delete() #borro usuario
    todos = Usuario.objects.all() #accedo a los usuarios de la BD actualizada sin usuario escogido
    return render(request,"AppCoder/usuarios.html", {"todos_usuarios":todos}) #contexto la nueva BD

#eliminar camara
def eliminar_camara(request, camara_marca): #envío nombre usuario que borraré
    marca_escogida = Camara.objects.get(marca = camara_marca) #usuario escogido es el nombre de la BD
    marca_escogida.delete() #borro usuario
    todos = Camara.objects.all() #accedo a los usuarios de la BD actualizada sin usuario escogido
    return render(request,"AppCoder/camaras.html", {"todas_camaras":todos}) #contexto la nueva BD

#eliminar tripode
def eliminar_tripode(request, tripode_marca): #envío nombre usuario que borraré
    marca_escogida = Tripode.objects.get(marca = tripode_marca) #usuario escogido es el nombre de la BD
    marca_escogida.delete() #borro usuario
    todos = Tripode.objects.all() #accedo a los usuarios de la BD actualizada sin usuario escogido
    return render(request,"AppCoder/tripodes.html", {"todos_tripode":todos}) #contexto la nueva BD

#eliminar telescopio
def eliminar_telescopio(request, telescopio_marca): #envío nombre usuario que borraré
    marca_escogida = Telescopio.objects.get(marca = telescopio_marca) #usuario escogido es el nombre de la BD
    marca_escogida.delete() #borro usuario
    todos = Telescopio.objects.all() #accedo a los usuarios de la BD actualizada sin usuario escogido
    return render(request,"AppCoder/telescopios.html", {"todos_telescopios":todos}) #contexto la nueva BD

#eliminar montura
def eliminar_montura(request, montura_marca): #envío nombre usuario que borraré
    marca_escogida = Montura.objects.get(marca = montura_marca) #usuario escogido es el nombre de la BD
    marca_escogida.delete() #borro usuario
    todos = Montura.objects.all() #accedo a los usuarios de la BD actualizada sin usuario escogido
    return render(request,"AppCoder/monturas.html", {"todas_montura":todos}) #contexto la nueva BD

#eliminar binocular
def eliminar_binocular(request, binocular_marca): #envío nombre usuario que borraré
    marca_escogida = Binocular.objects.get(marca = binocular_marca) #usuario escogido es el nombre de la BD
    marca_escogida.delete() #borro usuario
    todos = Binocular.objects.all() #accedo a los usuarios de la BD actualizada sin usuario escogido
    return render(request,"AppCoder/binoculares.html", {"todos_binoculares":todos}) #contexto la nueva BD


# ahora hay que complementar el url usuarios.html y crear un url

#falta una vista para actualizar!!!!!!!!!!!!!!!!!

# clase 23 Vista con Class
