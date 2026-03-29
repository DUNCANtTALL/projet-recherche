# Projet Recherche : Analyse comparative d'algorithmes d'optimisation

## Description
Ce dépôt contient les scripts, données et résultats pour l'analyse comparative de plusieurs algorithmes d'optimisation sur des problèmes BBOB.

## Organisation du dépôt
- `data/` : Données brutes et prétraitées (par étape)
- `scripts/` : Scripts Python et notebooks pour l'analyse
- `results/` : Figures, tableaux et résultats générés
- `requirements.txt` / `environment.yml` : Dépendances Python
- `LICENSE` : Licence d'utilisation

## Reproduire l'analyse
1. Cloner le dépôt
2. Installer les dépendances :
   - `pip install -r requirements.txt` ou `conda env create -f environment.yml`
3. Exécuter les scripts dans `scripts/` pour générer les résultats

## Données
Les données sont organisées par étape dans `data/Etape1`, `data/Etape2`, `data/Etape3`.

## Scripts
- `analyse_bbob.py` : Analyse d'un algorithme sur un problème
- `analyse_multi_algo.py` : Analyse comparative multi-algorithmes
- `convert_tdat_to_csv.py` : Conversion des fichiers .tdat en .csv
- `convert_etape3_to_csv.py` : Conversion des fichiers Etape3 en .csv
- `emulation_demarche.ipynb` : Notebook d'émulation de la démarche comparative

## Résultats
Les figures et tableaux générés sont dans `results/`.

## Licence
Voir le fichier `LICENSE`.

## Référence Zenodo


