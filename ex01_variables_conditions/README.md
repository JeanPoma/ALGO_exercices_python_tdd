# 01 – Variables & conditions

## 📋 Informations

- **Niveau** : ⭐ Débutant
- **Temps estimé** : 30-45 minutes
- **Prérequis** : Aucun (premier exercice)
- **Objectifs d'apprentissage** :
  - Manipuler les variables et types de base (int, float, str, bool)
  - Utiliser les opérateurs arithmétiques et de comparaison
  - Écrire des conditions simples et complexes
  - Gérer les cas limites et la validation des entrées
  - Comprendre les exceptions en Python

## 📝 Description

Ce premier exercice vous permet de prendre en main les concepts fondamentaux de Python : variables, expressions arithmétiques, conditions et robustesse du code. Vous allez implémenter des fonctions simples qui illustrent ces concepts de base.

## 🎯 Fonctions à implémenter

### Niveau 1 : Opérations de base
1. **`somme(a, b)`** - Additionner deux entiers
2. **`produit(a, b)`** - Multiplier deux entiers
3. **`est_pair(n)`** - Vérifier si un nombre est pair

### Niveau 2 : Conditions simples
4. **`est_voyelle(lettre)`** - Vérifier si une lettre est une voyelle (a, e, i, o, u, y)
5. **`calcul_reduction(prix, taux)`** - Calculer un prix après réduction avec validation
6. **`maximum_trois(a, b, c)`** - Trouver le maximum de trois valeurs sans utiliser `max()`

### Niveau 3 : Conditions complexes
7. **`est_bissextile(annee)`** - Déterminer si une année est bissextile (règle grégorienne)
8. **`racine_carree(x)`** - Calculer la racine carrée avec validation (lever exception si négatif)

### Niveau 4 : Algorithmes simples
9. **`factorielle(n)`** - Calculer la factorielle de manière itérative
10. **`convertir_en_binaire(n)`** - Convertir un entier en représentation binaire

## 🚀 Comment démarrer

1. Ouvrir le fichier `src/exercices.py`
2. Remplacer chaque `raise NotImplementedError` par votre implémentation
3. Lancer les tests pour vérifier votre solution :
   ```bash
   pytest -q ex01_variables_conditions
   ```

## 💡 Astuces

- **Modulo (%)** : Utilisez l'opérateur `%` pour vérifier la divisibilité
- **Validation** : Pensez à vérifier les cas limites (valeurs négatives, zéro, etc.)
- **Exceptions** : Utilisez `raise ValueError("message")` pour signaler les erreurs
- **Conditions multiples** : Utilisez `and`, `or`, `not` pour combiner les conditions

## 📚 Ressources

### Variables et types
- [Les variables en Python (OpenClassrooms)](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7291431-utilisez-des-variables-pour-stocker-vos-donnees)
- [Types de données Python (Documentation officielle)](https://docs.python.org/fr/3/library/stdtypes.html)

### Conditions
- [Les structures conditionnelles en Python](https://python.sdv.univ-paris-diderot.fr/04_tests/)
- [If, elif, else (W3Schools)](https://www.w3schools.com/python/python_conditions.asp)

### Opérateurs
- [Opérateurs arithmétiques et de comparaison](https://python.doctor/page-operateurs-python-operators-precedence)

### Algorithmes
- [Année bissextile - Explication (Wikipedia)](https://fr.wikipedia.org/wiki/Ann%C3%A9e_bissextile)
- [Factorielle - Introduction](https://fr.wikipedia.org/wiki/Factorielle)
- [Conversion binaire (Khan Academy)](https://fr.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/v/number-systems-introduction)

## ✅ Critères de réussite

- Tous les tests passent (11 tests)
- Les cas limites sont gérés correctement
- Les exceptions appropriées sont levées quand nécessaire
- Le code est lisible et bien structuré
