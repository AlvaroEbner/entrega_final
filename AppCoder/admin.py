from django.contrib import admin
from AppCoder.models import * #importar los modelos 


admin.site.register(Usuario)
admin.site.register(Fotografia)
admin.site.register(Tour)
admin.site.register(Camara)
admin.site.register(Tripode)
admin.site.register(Telescopio)
admin.site.register(Montura)
admin.site.register(Binocular)

#hacer visible la imagen del avatar
admin.site.register(Avatar)





# Register your models here.