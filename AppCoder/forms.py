from django import forms 


#Formularios

class Usuario_Form(forms.Form):
    nombre = forms.CharField(max_length=60) #str
    edad = forms.IntegerField() #int
    correo = forms.EmailField() #correo
    direccion = forms.CharField(max_length=60) #str
    
  
class Fotografia_Form(forms.Form): #consultar libro astrofotografia
   # tipo de campo para imagenes django???
    imagen = forms.ImageField() #imagen
    autor = forms.CharField(max_length=60)
    lugar = forms.CharField(max_length=60) 
    camara = forms.CharField(max_length=60) 
    objetivo = forms.CharField(max_length=60) 
    fecha = forms.DateTimeField() #corregir, el formulario no se ve en formato fecha
    iso = forms.IntegerField()
    diafragma_f = forms.FloatField()

class Reservar_tour_Fomr(forms.Form):
    nombre = forms.CharField(max_length=60) 
    total_adultos = forms.IntegerField()
    total_ninios = forms.IntegerField()
    #fecha_reserva = forms.DateTimeField(auto_now_add =True) #automáticamente la fecha y hora actual cuando se crea el objeto por primera vez y no se actualiza en futuras modificaciones
    fecha_tour = forms.DateField() 
    #opciones = [( 'observación','Observación'),('astrofotografia','Astrofotografía')]
    #tipo_tour = forms.CharField (max_length= 15, choices=opciones)

class Camara_Form(forms.Form):
    tipo = forms.ChoiceField (choices= [('reflex','Réflex'),('cielo_profundo','Cielo Profundo'),('planetaria','Planetaria')]) #reflex, cielo profundo, planetaria
    marca = forms.CharField(max_length=60) 
    precio = forms.IntegerField()
    color = forms.CharField(max_length=60) 



class Tripode_Form(forms.Form):
    marca = forms.CharField(max_length=60) 
    precio = forms.IntegerField()

  
class Telescopio_Form(forms.Form):
    tipo = forms.ChoiceField (choices= [ ( 'catadioptrico','Catadióptrico'), ( 'refractor','Refractor'),( 'newtoniano','Newtoniano')])  #catadióptrico, refractor, newtoniano
    apertura = forms.IntegerField()
    df = forms.IntegerField()
    f = forms.IntegerField()
    marca = forms.CharField(max_length=60) 


class Montura_Form(forms.Form):
    tipo = forms.ChoiceField (choices= [ ( 'azimutal','Azimutal'), ( 'ecuatorial','Ecuatorial')])#azimutal, ecuatorial
    seguimiento = forms.ChoiceField (choices= [ ( 'goto','GoTo'), ( 'manual','Manual')])
    carga_max = forms.IntegerField()
    marca = forms.CharField(max_length=60) 
    peso = forms.IntegerField()

class Binocular_Form(forms.Form):
    marca = forms.CharField(max_length=60) 
    apertura = forms.IntegerField()
    aumentos = forms.CharField(max_length=60) 
    peso =forms.IntegerField()
