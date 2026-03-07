PROYECTO FINAL DJANGO - LUCAS TRONCOSO
Este proyecto es para el curso de Python en Coderhouse. Es una web para gestionar un blog con usuarios, categorías y posts.

Activar el entorno: ..venv\Scripts\activate
Instalar Django: pip install django
Migrar la base de datos: python manage.py migrate
Correr el servidor: python manage.py runserver

Tengo 3 modelos: Usuario, Categoria y Post. Podés crear, ver, editar y borrar cualquiera de ellos.

Inicio (/): Ves la lista de posts y podés entrar a Editar o Eliminar.
Buscador (/buscar): Escribís el título de un post y te lo filtra.
Seccion About (/about): Info sobre mí y el proyecto.
Cuentas: Podés registrarte en /register y loguearte en /login.

DATOS DEL ADMIN
entrar al panel (/admin):
Usuario: admin
Clave: 123

Usé herencia de plantillas (base.html) para que todo el sitio tenga el mismo menú. El archivo .gitignore ya está configurado para que no se suba la carpeta del entorno virtual.