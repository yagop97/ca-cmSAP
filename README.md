# carga-masiva-SAP

Carga masiva de documentos de venta Camuzzi

## Instalación 🔧

Software necesario:
<ul>
  <li>Python 3.6 o superior 👉 <a href="https://www.python.org/downloads/">descargar</a></li>
  <li>Java para Windows 👉 <a href="https://www.java.com/es/download/ie_manual.jsp">descargar</a></li>
</ul>

Ambos deben estar incluidos en el PATH del sistema. <a href="https://www.java.com/es/download/help/path_es.html">Cómo cambiar variables del sistema</a>

Al momento de instalar python, ofrece la posibilidad de agregarlo al PATH del sistema (opción "Add Python 3.9 to PATH) 👇

![image](https://user-images.githubusercontent.com/84155397/126665001-5b8d2fe9-d690-4f3b-ac5a-45b2f6036e99.png)

Java no ofrece la opción de agregar al PATH al momento de la instalación, por lo que es necesario hacerlo manualmente. El directorio que debe agregarse al PATH (en caso de haber utilizado la carpeta de descarga por defecto):
```
C:\Program Files (x86)\Java\bin
```
## Descarga de archivos 📂
Descargar los archivos de este repositorio y extraer en alguna carpeta de la computadora. 

<a href="https://github.com/yagopajarino/ca-cmSAP/archive/refs/heads/main.zip">Descargar archivos</a>

Luego se debe abrir un CMD (Simbolo del sistema) en la carpeta donde están descargados los archivos, para ello:
<ol>
<li>Ctrl + L dentro de la carpeta -> sombrea la barra de directorio en color azul</li>
<li>Borrar lo sombreado en azul</li>
<li>Escribir CMD</li>
<li>Enter</li>
</ol>

Se debe abrir una pantalla como esta 👇

![image](https://user-images.githubusercontent.com/84155397/126667543-787fb8a6-12aa-4a75-a4de-5e9cf466abc7.png)

que en lugar de C:\Users debe tener la ruta de la carpeta donde se descargaron los archivos.

Una vez tenemos el CMD ubicado en la carpeta donde estan los archivos descargados, utilizamos el siguiente comando:
```
pip install -r requirements.txt
```
![image](https://user-images.githubusercontent.com/84155397/126671901-76f11023-a516-4b52-a2da-78e71b291656.png)

Al dar enter, comienza la descarga e instalación de las librerias necesarias.

## Utilización

1. Descargar de AFIP comprobantes emitidos para el periodo, guadar en la carpeta con el nombre <b>Mis Comprobantes Emitidos - CUIT 30657864281.xlsx</b>
2. Guadar los PDF de los comprobantes emitidos en la carpeta DOCS
3. Guardar el archivo CLIENTES.xlsx con numero de CUIT y codigo de SAP.
4. Hacer doble click en el archivo app.py

Al finalizar, se guarda el archivo llamado salida.xlsx

## Contacto
En caso de dudas, consutas, mejoras 👉 <a href="https://yagopajarino.github.io/repos-contact/?ca-cmSAP" target="_blank">Get in touch</a>

## Invitame un cafecito :money_with_wings:
Este repositorio es de uso libre bajo licencia MIT pero tu donación ayuda a mantenero y mejorarlo.

[![Invitame un café en cafecito.app](https://cdn.cafecito.app/imgs/buttons/button_3.svg)](https://cafecito.app/yagopajarino)

