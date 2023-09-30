# Tercera_pre-entrega_Ebner

1. lo primero es correr el servidor, abrir terminal: python3 manage.py runserver
2. copiar el siguiente url en el navegador: http://127.0.0.1:8000/AppCoder/, y se mostrará la pagina de inicio.
3. Esta página es la maqueta para ofrecer servicios de astro-turismo y venta de equipo de ésta índole.
4. Cada html (usuarios, galería de imágenes, Tour Astronómico, cámaras, trípodes, telescopio, monturas y binoculares) cuenta con un boton que envía a un html con un formulario para crear éste elemento.
5. al ir a : http://127.0.0.1:8000/AppCoder/usuarios/  o pinchar "usuarios" se despliegan las características de un CRUD de una base de datos: Se visualizan los usuarios, abajo hay un botón para crear usuario, el que envía a un formulario. También hay un botón para buscar usuarios, el que envía a un formulario de búsqueda. Por último, cada usuario contiene un botón para eliminar.
6. Al buscar un nombre de usuario que no esta en BD, se muestra: "No hay resultados que coincidan con tu búsqueda"
7. El proyecto tiene una aplicación AppCoder, el que contiene los archivos específicos.
8. Al modificar los modelos se debe migrar.
