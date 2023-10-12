# Comunidad de observación astronomica e intercambio de insumos: WENUMAPU

El proyecto es una pagina llamada wenumapu, que en lengua del pueblo mapuche es “la tierra de arriba”, la que tiene dos objetivos, el primero es agendar tour de observación astronómica o de astro-fotografía, y la otra es ofrecer equipamiento, el que pueden publicar tanto los usuarios como el administrador de la página.

## Descripción de los modelos.
- Usuario: Para el inicio de sesión, cerrar sesión, editar usuarios.

- Reservar: Tour (nombre, cantidad total de adultos, cantidad total de niños, fecha del tour con despliegue de calendario) éste modelo se aplica para publicar lista de reservas de tour en /tour.

- Modelos vinculados a equipamiento:
	- Cámara: (tipo para despliegue de opciones: réflex, cielo profundo, planetaria; marca; precio y 	color) este modelo se utiliza para desplegar lista de cámaras disponibles.  
	
	- Trípodes: (marca, precio) éste modelo se utiliza para desplegar lista de trípodes disponibles.

	- Telescopios: (Tipo para despliegue de opciones: catadióptrico, newtoniano o reflector; 	Apertura; Distancia Focal DF; Luminosidad F y marca) éste modelo se utiliza para listar 	telescopios disponibles.

	- Montura: (tipo para desplegar: azimutal, ecuatorial; Sistema de seguimiento Goto para 	desplegar opciones: manual, goto; Carga máxima, marca y peso.) este modelo se utiliza para 	publicar listado de monturas disponibles.

	-  Binoculares: (marca, apertura, aumentos, peso)

Cabe señalar que cada característica de los modelos está asociado a una entrada específica de tipo de información, ya sean str, int, float, fechas o despliegue de opciones.  

## Superuser.

- Nombre superuser: alvaro
- Contraseña: nada1234

## CRUD Create (Crear), Read (Leer), Update (Actualizar) y Delete (Borrar)

- Crear:  La primera opción de creación de objetos es el registro de usuario, al pinchar el link de registrarse en iniciar sesión, la otra opción de creación de objetos son los formularios en el apartado de equipamiento, aquí cada modelo de cámara, trípode, telescopio, montura y binocular tiene un botón para crear publicación, donde se despliega un formulario con las características.

- Leer:  En la pagina de Tour de observación y astro-fotografía y en cada pagina por cada equipo, se despliega una lista para ver los artículos que están publicados.

- Actualizar: Al iniciar sesión se despliega en la parte superior izquierda el link “Editar Usuario”, al pinchar se abre la pagina formulario para editar perfil de <nombre usuario> según el usuario actual. Éste formulario precarga el email y solicita contraseña, repetir contraseña, el primer y segundo nombre.

- Borrar:  En cada página de equipamiento: cámara, trípode, telescopio, montura y binocular, se despliega por cada elemento de la lista de artículos un botón azul que permite borrar el articulo asociado a la marca. Al pinchar éste botón se elimina el articulo y se actualizan los datos de la pagina.  
   

## Seguridad por medio del requisito de Iniciar sesión.

- En la página de inicio se despliega un mensaje que invita a iniciar sesión para agendar tour y ver los artículos publicados, puesto que los link Tour de Observación y Atrofotografía y el link de equipamientos están bloqueados, al pincha en ellos sin iniciar sesión se redirige a la pagina de inicio de sesión.

- Al pinchar el link de iniciar sesión se despliega el formulario solicitando nombre de usuario y contraseña, abajo se incluye un botón para iniciar sesión y otro para registrarse

- Solo esta disponible para ver sin iniciar sesión el link a la pagina Quién Soy.

- Una vez iniciada la sesión se pueden abrir todos los link y publicar por medio de los distintos formularios. Además se elimina el link para iniciar sesión, y en su lugar se mantiene el link de inicio, y emergen dos mas, uno para editar usuario y otro para cerrar sesión.

- Al pinchar el link de cerrar sesión, emerge un mensaje que señala que has cerrado sesión. Y pueden retornar a la pagina de inicio o iniciar sesión.

## Buscador

- En cada una de las 5 paginas donde se listan los artículos de equipamiento publicados (cámara, trípode, telescopio, montura y binocular), al final hay dos botones, uno para crear publicación y otro para buscar un artículo, al pinchar éste último, se despliega un formulario donde se debe indicar la marca del artículo para posteriormente pinchar el botón buscar, si la búsqueda es exitosa se despliega una lista con los artículos indicados. Si no existen coincidencias aparece el siguiente mensaje: No hay resultados que coincidan con tu búsqueda.

## Casos de Test
- Link planilla con registro de casos de test:  https://docs.google.com/spreadsheets/d/1n3ASjNMvhF2Dk-dQE29Lwl9J96n8xAmSy7jDOUIlCfE/edit?usp=sharing 


## Link Video de funcionalidad y navegación por la página.
- Video en formato mp4 pesa 81,5 mb
- Link al video publicado en youtube: https://youtu.be/WXtsUhPDNzU
- Link al video publicado en Drive para descargar: https://drive.google.com/file/d/1SpqfKsQ8nqXPCqd1LkRZPME00dceA8sF/view?usp=sharing 
