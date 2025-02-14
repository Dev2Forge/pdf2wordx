# pdf2docx 

![version-python](https://img.shields.io/badge/python->=3.6-green.svg)
<a target="_blank" href="https://codecov.io/gh/dothinking/pdf2docx"><img src="https://codecov.io/gh/dothinking/pdf2docx/branch/master/graph/badge.svg" alt="codecov"/></a>
<a target="_blank" href="https://pypi.python.org/pypi/pdf2docx/"><img src="https://img.shields.io/pypi/v/pdf2docx.svg" alt="version-pypi"/></a>
<img src="https://img.shields.io/pypi/l/pdf2docx.svg" alt="licence"/>
<img src="https://img.shields.io/pypi/dm/pdf2docx" alt="téléchargements-pypi"/>

- Extrait des données de PDF avec `PyMuPDF`, telles que du texte, des images et des dessins
- Analyse la mise en page avec des règles, telles que les sections, les paragraphes, les images et les tableaux
- Génère des docx avec `python-docx`

## Fonctionnalités

- Analyse et recrée la mise en page de la page
    - marges de page
    - sections et colonnes (seulement 1 ou 2 colonnes)
    - en-tête et pied de page [À FAIRE]

- Analyse et recrée les paragraphes
    - texte OCR [À FAIRE]
    - direction du texte horizontal/vertical : de gauche à droite, de bas en haut
    - style de police, par exemple, nom de la police, taille, poids, italique et couleur
    - formatage du texte, par exemple, surligner, souligner, barrer
    - style de liste [À FAIRE]
    - hyperlien externe
    - alignement horizontal du paragraphe (gauche/droite/centre/justifié) et espacement vertical
    
- Analyse et recrée les images
    - image en ligne
    - image en mode Gris/RGB/CMJN
    - image transparente
    - image flottante, c'est-à-dire image derrière le texte

- Analyse et recrée les tableaux
    - style de bordure, par exemple, largeur, couleur
    - style d’ombrage, c'est-à-dire, couleur de fond
    - cellules fusionnées
    - direction des cellules verticale
    - tableau avec des bordures partiellement cachées
    - tableaux imbriqués

- Analyse des pages avec traitement parallèle

*Peut également être utilisé comme un outil pour extraire le contenu des tableaux, car à la fois le contenu du tableau et le formatage/le style sont analysés.*

## Limitations

- Fichier PDF basé sur du texte
- Langue de gauche à droite
- Direction de lecture normale, sans transformation/rotation des mots
- Méthode basée sur des règles ne peut pas convertir entièrement la mise en page PDF

## Documentation

- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/installation.html">Installation</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.html">Guide de Démarrage Rapide</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.convert.html">Convertir PDF</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.table.html">Extraire Table</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.cli.html">Interface en Ligne de Commande</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.gui.html">Interface Graphique</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/techdoc.html">Documentation Technique (En Chinois)</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/modules.html">Documentation de l'API</a>

## Échantillon

<div style="" class="centered">
    <img style="filter: drop-shadow(5px 5px 4px var(--body-color))" width=80% src="https://github.com/tutosrive/images-projects-srm-trg/raw/main/pdf2docx/sample-pdf2docx.png">
</div>