# 03 – Fonctions & algorithmes célèbres

## 📋 Informations

- **Niveau** : ⭐⭐⭐ Intermédiaire
- **Temps estimé** : 2h-3h
- **Prérequis** : Exercices 01 et 02 (conditions, boucles, listes)
- **Objectifs d'apprentissage** :
  - Créer et utiliser des fonctions Python
  - Implémenter des algorithmes classiques (PGCD, Fibonacci, nombres premiers)
  - Comprendre la récursivité vs itération
  - Maîtriser les algorithmes de recherche (recherche binaire)
  - Analyser la complexité algorithmique

## 📝 Description

Cet exercice vous initie aux algorithmes classiques de l'informatique et à la programmation fonctionnelle. Vous allez implémenter des fonctions utilitaires simples puis des algorithmes célèbres, d'abord de manière itérative puis récursive pour comparer les deux approches.

## 🎯 Fonctions à implémenter

### 🔰 Prise en main (6 fonctions)
Manipulation de base des fonctions :
1. **`print_hello_world()`** - Afficher "Hello, world!"
2. **`reverse_string(param)`** - Inverser une chaîne
3. **`to_uppercase(param)`** - Convertir en majuscules
4. **`count_substring(param, sub)`** - Compter les occurrences d'une sous-chaîne
5. **`list_length(param)`** - Longueur d'une liste
6. **`max_in_list(param)`** - Maximum dans une liste

### 🧮 Algorithmes classiques - Version itérative (5 fonctions)
7. **`pgcd(a, b)`** - Plus Grand Commun Diviseur (algorithme d'Euclide)
8. **`fibonacci(n)`** - nième nombre de Fibonacci
9. **`crible_eratosthene(n)`** - Générer tous les nombres premiers jusqu'à n
10. **`is_prime(n)`** - Vérifier si un nombre est premier
11. **`is_palindrome(s)`** - Vérifier si une chaîne est un palindrome
12. **`binary_search(arr, target)`** - Recherche binaire dans une liste triée

### 🔄 Algorithmes récursifs (5 fonctions)
Mêmes algorithmes en version récursive :
13. **`gcd_recursive(a, b)`** - PGCD récursif
14. **`fibonacci_recursive(n)`** - Fibonacci récursif
15. **`is_prime_recursive(n, divisor)`** - Vérification de primalité récursive
16. **`is_palindrome_recursive(s)`** - Palindrome récursif
17. **`factorial_recursive(n)`** - Factorielle récursive

## 🚀 Comment démarrer

1. Ouvrir le fichier `src/exercices.py`
2. Commencer par les fonctions simples puis progresser vers les algorithmes
3. Implémenter d'abord les versions itératives, puis les récursives
4. Lancer les tests :
   ```bash
   pytest -q ex03_fonctions_algo
   ```

## 💡 Astuces

### Fonctions
- **Définition** : `def nom_fonction(parametres): ...`
- **Retour** : Utilisez `return` pour renvoyer une valeur
- **Docstrings** : Documentez vos fonctions avec des chaînes de documentation

### Algorithme d'Euclide (PGCD)
- Tant que `b ≠ 0` : `a, b = b, a % b`
- Retourner `a` quand `b = 0`

### Crible d'Ératosthène
1. Créer une liste booléenne de taille n+1
2. Marquer 0 et 1 comme non premiers
3. Pour chaque nombre premier p, marquer tous ses multiples comme non premiers
4. Extraire les nombres marqués comme premiers

### Recherche binaire
- Nécessite une liste **triée**
- Diviser l'espace de recherche par 2 à chaque itération
- Complexité : O(log n)

### Récursivité
- **Cas de base** : Condition d'arrêt obligatoire
- **Cas récursif** : Appel de la fonction elle-même avec un problème plus petit
- **Attention** : Risque de stack overflow si trop d'appels

## 📚 Ressources

### Fonctions
- [Définir des fonctions en Python](https://docs.python.org/fr/3/tutorial/controlflow.html#defining-functions)
- [Les fonctions (OpenClassrooms)](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7291476-creez-votre-premiere-fonction)

### Algorithme d'Euclide
- [PGCD - Algorithme d'Euclide (Wikipedia)](https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide)
- [Euclid's Algorithm (Khan Academy)](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)

### Suite de Fibonacci
- [Suite de Fibonacci (Wikipedia)](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci)
- [Fibonacci en Python](https://realpython.com/fibonacci-sequence-python/)

### Nombres premiers
- [Crible d'Ératosthène (Wikipedia)](https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne)
- [Prime Numbers Algorithm](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)
- [Test de primalité](https://fr.wikipedia.org/wiki/Test_de_primalit%C3%A9)

### Recherche binaire
- [Binary Search Algorithm](https://www.geeksforgeeks.org/binary-search/)
- [Recherche dichotomique (Wikipedia)](https://fr.wikipedia.org/wiki/Recherche_dichotomique)

### Récursivité
- [Récursivité en Python](https://python.sdv.univ-paris-diderot.fr/12_recursivite/)
- [Understanding Recursion (Real Python)](https://realpython.com/python-thinking-recursively/)

## ✅ Critères de réussite

- Tous les tests passent (16 tests)
- Comprendre la différence entre itération et récursion
- Code optimisé et efficace
- Gestion correcte des cas limites
- Complexité algorithmique appropriée

## 🎓 Pour aller plus loin

- Comparer les performances itératives vs récursives avec `timeit`
- Implémenter la mémoïsation pour optimiser Fibonacci récursif
- Étudier d'autres algorithmes : tri rapide, tri fusion, recherche de motifs
