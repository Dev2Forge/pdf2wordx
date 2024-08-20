# pdf2docx 

![versión-python](https://img.shields.io/badge/python->=3.6-green.svg)
<a target="_blank" href="https://codecov.io/gh/dothinking/pdf2docx"><img src="https://codecov.io/gh/dothinking/pdf2docx/branch/master/graph/badge.svg" alt="codecov"/></a>
<a target="_blank" href="https://pypi.python.org/pypi/pdf2docx/"><img src="https://img.shields.io/pypi/v/pdf2docx.svg" alt="versión-pypi"/></a>
<img src="https://img.shields.io/pypi/l/pdf2docx.svg" alt="licencia"/>
<img src="https://img.shields.io/pypi/dm/pdf2docx" alt="descargas-pypi"/>

- Extrae datos de PDF con `PyMuPDF`, por ejemplo, texto, imágenes y dibujos
- Analiza el diseño con reglas, por ejemplo, secciones, párrafos, imágenes y tablas
- Genera docx con `python-docx`

## Características

- Analiza y recrea el diseño de la página
    - márgenes de página
    - secciones y columnas (solo 1 o 2 columnas)
    - encabezado y pie de página [POR HACER]

- Analiza y recrea párrafos
    - texto OCR [POR HACER]
    - texto en dirección horizontal/vertical: de izquierda a derecha, de abajo hacia arriba
    - estilo de fuente, por ejemplo, nombre de fuente, tamaño, peso, cursiva y color
    - formato de texto, por ejemplo, resaltar, subrayar, tachado
    - estilo de lista [POR HACER]
    - hipervínculo externo
    - alineación horizontal del párrafo (izquierda/derecha/centro/justificado) y espaciado vertical
    
- Analiza y recrea imágenes
	- imagen en línea
    - imagen en modo Gris/RGB/CMYK
    - imagen transparente
    - imagen flotante, es decir, imagen detrás del texto

- Analiza y recrea tablas
    - estilo de borde, por ejemplo, ancho, color
    - estilo de sombreado, es decir, color de fondo
    - celdas fusionadas
    - celda en dirección vertical
    - tabla con bordes parcialmente ocultos
    - tablas anidadas

- Análisis de páginas con procesamiento en paralelo

*También se puede utilizar como una herramienta para extraer contenidos de tablas, ya que tanto el contenido de la tabla como el formato/estilo se analizan.*

## Limitaciones

- Archivo PDF basado en texto
- Idioma de izquierda a derecha
- Dirección de lectura normal, sin transformación / rotación de palabras
- El método basado en reglas no puede convertir al 100% el diseño del PDF

## Documentación

- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/installation.html">Instalación</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.html">Guía Rápida</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.convert.html">Convertir PDF</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.table.html">Extraer tabla</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.cli.html">Interfaz de Línea de Comandos</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.gui.html">Interfaz Gráfica de Usuario</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/techdoc.html">Documentación Técnica (En Chino)</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/modules.html">Documentación de la API</a>

## Muestra

<div style="" class="centered">
    <img style="filter: drop-shadow(5px 5px 4px var(--body-color))" width=80% src="https://github.com/tutosrivegamerLQ/images-projects-srm-trg/raw/main/pdf2docx/sample-pdf2docx.png">
</div>