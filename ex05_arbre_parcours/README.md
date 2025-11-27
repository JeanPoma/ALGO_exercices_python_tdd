# 05 – Algorithmes de parcours d'arbre

## 📋 Informations

- **Niveau** : ⭐⭐⭐⭐ Avancé
- **Temps estimé** : 2h-2h30
- **Prérequis** : Exercices 01, 02 et 03 (récursivité, structures de données)
- **Objectifs d'apprentissage** :
  - Comprendre les structures d'arbres binaires
  - Maîtriser les différents types de parcours (DFS, BFS)
  - Implémenter des parcours récursifs et itératifs
  - Utiliser les piles et files pour les parcours
  - Analyser les différences entre parcours en profondeur et en largeur

## 📝 Description

Cet exercice vous apprend à parcourir des arbres binaires de différentes manières. Vous allez implémenter 6 fonctions de parcours : préfixe, infixe, suffixe (récursifs) et DFS/BFS (itératifs avec pile/file). Ces algorithmes sont fondamentaux pour manipuler les structures hiérarchiques.

## 🎯 Fonctions à implémenter

### 🌳 Parcours récursifs (3 fonctions)
1. **`parcours_prefixe(racine)`** - Parcours pré-ordre (racine → gauche → droit)
2. **`parcours_infixe(racine)`** - Parcours in-ordre (gauche → racine → droit)
3. **`parcours_suffixe(racine)`** - Parcours post-ordre (gauche → droit → racine)

### 🔄 Parcours itératifs (3 fonctions)
4. **`parcours_dfs(racine)`** - Depth-First Search avec pile
5. **`parcours_bfs(racine)`** - Breadth-First Search avec file
6. **`parcours_largeur(racine)`** - Alias de BFS (parcours par niveaux)

## 🚀 Comment démarrer

1. Étudier la classe `Node` dans `common/tree.py`
2. Ouvrir le fichier `src/parcours.py`
3. Implémenter les parcours un par un
4. Lancer les tests :
   ```bash
   pytest -q ex05_arbre_parcours
   ```

## 💡 Astuces

### Structure d'arbre
```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left    # Sous-arbre gauche
        self.right = right  # Sous-arbre droit
```

### Parcours récursifs
- **Préfixe** : Visiter racine, puis gauche, puis droit
- **Infixe** : Visiter gauche, puis racine, puis droit (donne ordre trié pour BST)
- **Suffixe** : Visiter gauche, puis droit, puis racine

### Parcours itératifs
- **DFS (pile)** : LIFO - Last In First Out, explorer en profondeur
- **BFS (file)** : FIFO - First In First Out, explorer par niveau

### Collections Python utiles
- **Liste comme pile** : `append()` pour empiler, `pop()` pour dépiler
- **`collections.deque`** : Efficace pour les files (`append()`, `popleft()`)

## 📚 Ressources - Algorithmes de parcours d'arbre

Voici une description de chaque algorithme inclus dans ce répertoire. Chaque description comprend une explication du
fonctionnement de l’algorithme ainsi que des ressources pour faciliter l’apprentissage.

#### 1. **Parcours en profondeur (DFS - Depth First Search)**

- **Explication** :
  Le parcours en profondeur visite un nœud, puis explore aussi loin que possible sur chacun de ses voisins avant de
  revenir en arrière. Cela peut être implémenté en utilisant une pile (stack) ou une récursion. L'objectif est de
  parcourir systématiquement tous les chemins possibles pour atteindre un certain point, voire explorer la totalité de
  l’arbre/graphes.
- **Applications** :
    - Résoudre des puzzles (ex. labyrinthes)
    - Recherche de chemins dans un graphe
- **Ressources** :
    - [Visualisation du DFS (vidéo YouTube)](https://youtu.be/oLONftTvpHI)
    - [Explication détaillée sur GeeksForGeeks](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)

#### 2. **Parcours en largeur (BFS - Breadth First Search)**

- **Explication** :
  Le parcours en largeur explore un nœud, puis tous ses voisins directs avant de passer à leurs voisins. Cela peut être
  implémenté en utilisant une file (queue). Contrairement au DFS, le BFS explore un par un chaque niveau d’un
  graphe/arbre avant de descendre plus profondément.
- **Applications** :
    - Trouver le chemin le plus court dans un graphe non pondéré
    - Recommandations sociales basées sur la proximité (par exemple, amis communs)
- **Ressources** :
    - [Animation et explication du BFS (vidéo YouTube)](https://youtu.be/UuEJM8YXU7Y)
    - [Documentation sur BFS sur Programiz](https://www.programiz.com/dsa/graph-bfs)

#### 3. **Parcours en ordre (In-order Traversal)**

- **Explication** :
  Dans un parcours in-order, les nœuds d’un arbre binaire sont visités dans l’ordre suivant : sous-arbre gauche, racine,
  sous-arbre droit. Cela convient particulièrement aux arbres de recherche binaire (BST) où les valeurs sont renvoyées
  dans l’ordre croissant.
- **Applications** :
    - Extraction triée d’un arbre de recherche binaire
    - Conversion en collection triée ou traitement séquentiel
- **Ressources** :
    - [Basics and Animation of In-order Traversal (video)](https://youtu.be/G_38iNg0R44)
    - [Tutoriel Interactif Traversal Tree](https://visualgo.net/en/dfsbfs)

#### 4. **Parcours pré-ordre (Pre-order Traversal)**

- **Explication** :
  Ici, chaque nœud est visité avant ses sous-arbres. L’ordre est : racine, sous-arbre gauche, sous-arbre droit, ce qui
  se fait de manière récursive ou via une pile.
- **Applications** :
    - Copier un arbre
    - Conversion en structure linéaire ordonnée
- **Ressources** :
    - [Pre-order Traversal Visualization](https://youtu.be/VHgiIJp-OkY)

## ✅ Critères de réussite

- Tous les tests passent (6 fonctions de parcours testées)
- Comprendre les différences entre parcours récursifs et itératifs
- Maîtriser l'utilisation de piles et files
- Code efficace et lisible
- Gestion correcte des arbres vides (None)
