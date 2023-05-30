# MLOpsConsumoPragmatic

Generacion del scaffold o estructura de DevOps
image.png

Asegurarse de hacer uso del Command Prompt (cmd)
1. Creacion del ambiente virtual en Python python3 -m venv nombrevenv o py venv -m nombrevenv
 y activacion: venv\Scripts\activate

2. Creacion de archivos vacios comando: type nul > requirements.txt, type nul > Dockerfile, type nul > Makefile 
3. Creacion de una libreria en la que almacenar: md mylib y crear archivo para iniciarlo: type nul > mylib/__init__.py
4. Creacion de un archivo en el que se encuentra la logica del programa: type nul > mylib/logic.py y creacion del archivo main.py: type nul > main.py

image.png

5. Llenar el archivo Makefile que es el que tiene los pasos del proyecto desde DevOps
6. Diligenciar el archivo requirements.txt con las librerias requeridas, usar freeze para establecer las versiones
7. Crear un workflow en las acciones del repositorio de GitHub, como el archivo devops.yml. Ejecutar.
8. Creacion de archivo para uso de fire cli-fire.py
9. Ejecutar el archivo fire con comando: chmod +x cli-fire.py para despues hacer ./cli-fire.py --help Esto es para brindar info de las funciones ejecutadas como el nombre, sinopsis, descripcion y flags, lo que se esta haciendo es probar la logica. Se pueden pasar los parametros de las funciones con el uso de ./cli-fire.py --name "Barack Obama"
10. 

