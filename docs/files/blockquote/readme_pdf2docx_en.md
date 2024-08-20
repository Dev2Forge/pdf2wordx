# pdf2docx 

![python-version](https://img.shields.io/badge/python->=3.6-green.svg)
<a target="_blank" href="https://codecov.io/gh/dothinking/pdf2docx"><img src="https://codecov.io/gh/dothinking/pdf2docx/branch/master/graph/badge.svg" alt="codecov"/></a>
<a target="_blank" href="https://pypi.python.org/pypi/pdf2docx/"><img src="https://img.shields.io/pypi/v/pdf2docx.svg" alt="pypi-version"/></a>
<img src="https://img.shields.io/pypi/l/pdf2docx.svg" alt="license"/>
<img src="https://img.shields.io/pypi/dm/pdf2docx" alt="downloads-pypi"/>

- Extracts data from PDF with `PyMuPDF`, such as text, images, and drawings
- Analyzes layout with rules, such as sections, paragraphs, images, and tables
- Generates docx with `python-docx`

## Features

- Analyzes and recreates page layout
    - page margins
    - sections and columns (only 1 or 2 columns)
    - header and footer [TO DO]

- Analyzes and recreates paragraphs
    - OCR text [TO DO]
    - text direction horizontal/vertical: left to right, bottom to top
    - font style, e.g., font name, size, weight, italic, and color
    - text formatting, e.g., highlight, underline, strikethrough
    - list style [TO DO]
    - external hyperlink
    - horizontal alignment of the paragraph (left/right/center/justified) and vertical spacing
    
- Analyzes and recreates images
    - inline image
    - image in Grayscale/RGB/CMYK mode
    - transparent image
    - floating image, i.e., image behind text

- Analyzes and recreates tables
    - border style, e.g., width, color
    - shading style, i.e., background color
    - merged cells
    - vertical cell direction
    - table with partially hidden borders
    - nested tables

- Page analysis with parallel processing

*Can also be used as a tool for extracting table contents, as both table content and formatting/style are analyzed.*

## Limitations

- Text-based PDF file
- Left-to-right language
- Normal reading direction, without word transformation/rotation
- Rule-based method cannot fully convert PDF layout

## Documentation

- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/installation.html">Installation</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.html">Quick Start</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.convert.html">Convert PDF</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.table.html">Extract Table</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.cli.html">Command Line Interface</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.gui.html">Graphical User Interface</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/techdoc.html">Technical Documentation (In Chinese)</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/modules.html">API Documentation</a>

## Sample

<div style="" class="centered">
    <img style="filter: drop-shadow(5px 5px 4px var(--body-color))" width=80% src="https://github.com/tutosrivegamerLQ/images-projects-srm-trg/raw/main/pdf2docx/sample-pdf2docx.png">
</div>