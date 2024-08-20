# pdf2docx 

![версия-python](https://img.shields.io/badge/python->=3.6-green.svg)
<a target="_blank" href="https://codecov.io/gh/dothinking/pdf2docx"><img src="https://codecov.io/gh/dothinking/pdf2docx/branch/master/graph/badge.svg" alt="codecov"/></a>
<a target="_blank" href="https://pypi.python.org/pypi/pdf2docx/"><img src="https://img.shields.io/pypi/v/pdf2docx.svg" alt="версия-pypi"/></a>
<img src="https://img.shields.io/pypi/l/pdf2docx.svg" alt="лицензия"/>
<img src="https://img.shields.io/pypi/dm/pdf2docx" alt="скачивания-pypi"/>

- Извлекает данные из PDF с помощью `PyMuPDF`, такие как текст, изображения и рисунки
- Анализирует макет с помощью правил, таких как секции, абзацы, изображения и таблицы
- Генерирует docx с помощью `python-docx`

## Особенности

- Анализирует и воссоздает макет страницы
    - поля страницы
    - секции и колонки (только 1 или 2 колонки)
    - верхний и нижний колонтитулы [В РАБОТЕ]

- Анализирует и воссоздает абзацы
    - текст OCR [В РАБОТЕ]
    - направление текста горизонтальное/вертикальное: слева направо, снизу вверх
    - стиль шрифта, например, имя шрифта, размер, вес, курсив и цвет
    - форматирование текста, например, выделение, подчеркивание, зачеркивание
    - стиль списка [В РАБОТЕ]
    - внешний гиперссылка
    - горизонтальное выравнивание абзаца (слева/справа/по центру/по ширине) и вертикальное расстояние
    
- Анализирует и воссоздает изображения
    - встроенное изображение
    - изображение в режиме оттенков серого/RGB/CMYK
    - прозрачное изображение
    - плавающее изображение, т.е. изображение за текстом

- Анализирует и воссоздает таблицы
    - стиль границы, например, ширина, цвет
    - стиль затенения, т.е. цвет фона
    - объединенные ячейки
    - вертикальное направление ячейки
    - таблица с частично скрытыми границами
    - вложенные таблицы

- Анализ страниц с параллельной обработкой

*Также можно использовать как инструмент для извлечения содержимого таблиц, поскольку как содержимое таблицы, так и форматирование/стиль анализируются.*

## Ограничения

- Текстовый PDF-файл
- Язык слева направо
- Обычное направление чтения, без преобразования/вращения слов
- Метод на основе правил не может полностью преобразовать макет PDF

## Документация

- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/installation.html">Установка</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.html">Быстрый старт</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.convert.html">Конвертировать PDF</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.table.html">Извлечь таблицу</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.cli.html">Командная строка</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.gui.html">Графический интерфейс</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/techdoc.html">Техническая документация (На китайском)</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/modules.html">Документация API</a>

## Пример

<div style="" class="centered">
    <img style="filter: drop-shadow(5px 5px 4px var(--body-color))" width=80% src="https://github.com/tutosrivegamerLQ/images-projects-srm-trg/raw/main/pdf2docx/sample-pdf2docx.png">
</div>