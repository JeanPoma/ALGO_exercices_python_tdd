# 06 – Algorithme du Voyageur de Commerce (TSP)

## 📋 Informations

- **Niveau** : ⭐⭐⭐⭐⭐ Expert
- **Temps estimé** : 3h-4h
- **Prérequis** : Tous les exercices précédents (récursivité, optimisation, complexité)
- **Objectifs d'apprentissage** :
  - Comprendre les problèmes NP-complets
  - Implémenter plusieurs approches d'optimisation
  - Comparer brute force, heuristiques et métaheuristiques
  - Maîtriser la programmation dynamique
  - Découvrir les algorithmes génétiques

## 📝 Introduction

Le problème du voyageur de commerce (TSP - Travelling Salesman Problem) est un problème classique en optimisation
combinatoire. Il consiste à trouver le chemin le plus court permettant à un voyageur de visiter une liste donnée de
villes exactement une fois, puis de revenir à son point de départ.

**Complexité** : NP-complet - le temps de résolution croît exponentiellement avec le nombre de villes.

## 🎯 Fonctions à implémenter

### Utilitaires (2 fonctions)
1. **`generate_cities()`** - Générer un ensemble de villes (coordonnées aléatoires)
2. **`calculate_distance(city1, city2)`** - Calculer la distance euclidienne entre deux villes

### Algorithmes de résolution (4 fonctions)
3. **`brute_force_tsp(cities)`** - Approche exhaustive (toutes les permutations)
4. **`optimize_with_greedy(cities)`** - Heuristique gloutonne (plus proche voisin)
5. **`optimize_with_dynamic_programming(cities)`** - Programmation dynamique (Held-Karp)
6. **`optimize_with_genetic_algorithm(cities)`** - Algorithme génétique

## 🚀 Comment démarrer

1. Comprendre le problème et les différentes approches
2. Implémenter d'abord les fonctions utilitaires
3. Commencer par brute force (petit nombre de villes)
4. Progresser vers les méthodes optimisées
5. Lancer les tests :
   ```bash
   pytest -q ex06_voyageur_commerce
   ```

## 💡 Approches pour résoudre le TSP

1. **Méthodes exactes** : Ces approches garantissent de trouver la solution optimale mais sont souvent coûteuses en
   termes de temps de calcul pour de grandes instances.
    - Exemple : Programmation dynamique (ex. algorithme de Held-Karp).

2. **Méthodes d'approximation** : Ces algorithmes fournissent des solutions approchées et sont souvent plus rapides.
    - Heuristiques comme Nearest Neighbor ou Minimum Spanning Tree.
    - Métaheuristiques comme **Ant Colony Optimization** ou **Simulated Annealing**.

## 💡 Astuces par algorithme

### Distance euclidienne
```python
import math
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
```

### Brute Force
- Utiliser `itertools.permutations()` pour générer toutes les permutations
- Limité à ~10 villes maximum (10! = 3,628,800 permutations)

### Greedy (Plus proche voisin)
1. Commencer à une ville de départ
2. À chaque étape, aller à la ville non visitée la plus proche
3. Revenir au point de départ
- Rapide mais pas optimal (approximation)

### Programmation dynamique (Held-Karp)
- Utiliser la mémoïsation pour éviter les recalculs
- Complexité : O(n² × 2ⁿ) - mieux que brute force O(n!)
- Faisable jusqu'à ~20 villes

### Algorithme génétique
1. Population initiale de chemins aléatoires
2. Sélection des meilleurs chemins (fitness = distance inverse)
3. Croisement (crossover) de chemins parents
4. Mutation aléatoire
5. Répéter pendant N générations

## ✅ Critères de réussite

- Tous les tests passent (6 fonctions)
- Comprendre les compromis temps/qualité de solution
- Implémenter au moins 3 approches différentes
- Mesurer et comparer les performances
- Code optimisé et bien documenté

## 📚 Utilisation en Python et ressources

Le TSP est fréquemment implémenté en Python pour illustrer des approches diverses.

Ajoutez cette section pour enrichir votre exploration des différentes techniques mentionnées plus haut !

Voici quelques ressources utiles pour en apprendre davantage sur l'algorithme du voyageur de commerce et comment le
résoudre en Python :

1. [Travelling Salesman Problem (TSP) - GeeksforGeeks](https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/)
    - Une introduction détaillée au TSP, avec des explications sur les approches exactes et des exemples de code en
      Python.

2. [Tutoriel Python TSP avec heuristiques (Ant Colony Optimization)](https://towardsdatascience.com/solving-traveling-salesman-problem-with-python-optimization-tools-2021-cb93cba581b2)
    - Une explication pas à pas pour utiliser des heuristiques, avec du code Python.

3. [GitHub - Exemples de TSP en Python](https://github.com/search?q=travelling+salesman+python)
    - Une collection de projets open-source sur GitHub pour voir des exemples concrets d'implémentations.

Ces ressources devraient vous aider à mieux comprendre et à vous initier à l'implémentation du TSP en Python.
