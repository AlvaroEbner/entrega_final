# Comunidad de observación astronomica e intercambio de insumos: WENUMAPU (la tierra del cielo)

El proyecto es una pagina web que tiene dos objetivos, el primero es agendar tour de observación astronómica y la otra es ofrecer equipamiento, el que pueden ofrecer los usuarios de la plataforma.

##Descripción de los modelos.
- Usuario: Para el inicio de sesión, cerrar sesión, editar usuarios.

- Reservar: Tour (nombre, cantidad total de adultos, cantidad total de niños, fecha del tour con despliegue de calendario) éste modelo se aplica para publicar lista de reservas de tour en /tour.

- Modelos vinculados a equipamiento:
	- Cámara: (tipo y se despliegan opciones, marca, precio, color) este modelo se 





Tercera_pre-entrega_Ebner

1. lo primero es correr el servidor, abrir terminal: python3 manage.py runserver
2. copiar el siguiente url en el navegador: http://127.0.0.1:8000/AppCoder/, y se mostrará la pagina de inicio.
3. Esta página es la maqueta para ofrecer servicios de astro-turismo y venta de equipo de ésta índole.
4. Cada html (usuarios, galería de imágenes, Tour Astronómico, cámaras, trípodes, telescopio, monturas y binoculares) cuenta con un boton que envía a un html con un formulario para crear éste elemento.
5. al ir a : http://127.0.0.1:8000/AppCoder/usuarios/  o pinchar "usuarios" se despliegan las características de un CRUD de una base de datos: Se visualizan los usuarios, abajo hay un botón para crear usuario, el que envía a un formulario. También hay un botón para buscar usuarios, el que envía a un formulario de búsqueda. Por último, cada usuario contiene un botón para eliminar.
6. Al buscar un nombre de usuario que no esta en BD, se muestra: "No hay resultados que coincidan con tu búsqueda"
7. El proyecto tiene una aplicación AppCoder, el que contiene los archivos específicos.
8. Al modificar los modelos se debe migrar.

 ## Subtitulo
- [Acerca del Proyecto](#acerca-del-proyecto)
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribución](#contribución)
- [Licencia](#licencia)

- 
-readme.md
	- descripción: para que es el proyecto, explicar los crud
	- nombre del proyecto, objetivos, y los modelos funcionales.
	- superusuario y contraseña se debe incorporar.
	- se deben mencionar los modelos.
	- Pruebas realizadas, link a las pruebas
	- video demostración (link)
	- 
