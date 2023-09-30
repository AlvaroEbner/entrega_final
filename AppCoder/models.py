from django.db import models

#modelos para pagina Astroturismo

class Usuario(models.Model):
    nombre = models.CharField(max_length=60) #str
    edad = models.IntegerField() #int
    correo = models.EmailField() #correo
    direccion = models.CharField(max_length=60) #str
    

class Fotografia(models.Model): #consultar libro astrofotografia
   # tipo de campo para imagenes django???
    imagen = models.ImageField() #imagen
    autor = models.CharField(max_length=60)
    lugar = models.CharField(max_length=60) 
    camara = models.CharField(max_length=60) 
    objetivo = models.CharField(max_length=60) 
    fecha = models.DateField()
    iso = models.IntegerField()
    diafragma_f = models.FloatField()

class Tour(models.Model):
    nombre = models.CharField(max_length=60) 
    total_adultos = models.IntegerField()
    total_ninios = models.IntegerField()
    #fecha_reserva = models.DateTimeField(auto_now_add =True) #automáticamente la fecha y hora actual cuando se crea el objeto por primera vez y no se actualiza en futuras modificaciones
    fecha_tour = models.DateField() 
    #opciones = [( 'observación','Observación'),('astrofotografia','Astrofotografía')]
    #tipo_tour = models.CharField (max_length= 15, choices=opciones) #despliege opcion (observación o astrofoto) /Cada tupla contiene dos elementos: el valor que se enviará al servidor cuando se seleccione esa opción y la etiqueta que se mostrará al usuario.


class Camara(models.Model):
    opciones = [( 'reflex','Reflex'), ( 'cielo_profundo','Cielo Profundo'),( 'planetaria','Planetaria')]
    
    tipo = models.CharField(max_length= 15, choices=opciones)  #reflex, cielo profundo, planetaria
    marca = models.CharField(max_length=60) 
    precio = models.IntegerField()
    color = models.CharField(max_length=60) 
    
class Tripode(models.Model):
    marca = models.CharField(max_length=60) 
    precio = models.IntegerField()
    
class Telescopio(models.Model):
    opciones = [( 'catadioptrico','Catadióptrico'), ( 'refractor','Refractor'),( 'newtoniano','Newtoniano')]
    
    tipo = models.CharField(max_length= 15, choices=opciones)   #catadióptrico, refractor, newtoniano
    apertura = models.IntegerField()
    df = models.IntegerField()
    f = models.IntegerField()
    marca = models.CharField(max_length=60) 

class Montura(models.Model):
    opciones_1 = [( 'azimutal','Azimutal'), ( 'ecuatorial','Ecuatorial')]
    opciones_2 =[( 'goto','GoTo'), ( 'manual','Manual')]
    tipo = models.CharField  (max_length= 15 , choices= opciones_1)  #azimutal, ecuatorial
    goto = models.CharField  (max_length= 15 , choices= opciones_2) 
    carga_max = models.IntegerField()
    marca = models.CharField(max_length=60) 
    peso = models.IntegerField()

class Binocular(models.Model):
    marca = models.CharField(max_length=60) 
    apertura = models.IntegerField()
    aumentos = models.CharField(max_length=60) 
    peso =models.IntegerField()







