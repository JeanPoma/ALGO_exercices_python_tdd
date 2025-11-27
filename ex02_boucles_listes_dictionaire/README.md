# 02 – Boucles, listes & dictionnaires

## 📋 Informations

- **Niveau** : ⭐⭐ Débutant-Intermédiaire
- **Temps estimé** : 1h30-2h
- **Prérequis** : Exercice 01 (variables et conditions)
- **Objectifs d'apprentissage** :
  - Maîtriser les boucles `for` et `while`
  - Manipuler les collections Python (listes, tuples, sets, dictionnaires)
  - Comprendre les différences entre structures mutables et immutables
  - Appliquer des opérations courantes sur les collections
  - Utiliser les méthodes natives des structures de données

## 📝 Description

Cet exercice approfondit la manipulation des structures de données fondamentales de Python. Vous allez implémenter 34 fonctions couvrant les opérations courantes sur les listes, tuples, sets et dictionnaires. L'objectif est de comprendre les spécificités de chaque structure et savoir choisir la plus adaptée.

## 🎯 Fonctions à implémenter

### 📦 Listes (14 fonctions)
Opérations sur les listes mutables :
1. **`somme_pairs(nums)`** - Somme des nombres pairs
2. **`compter_occurrences(items, valeur)`** - Compter les occurrences d'une valeur
3. **`table_multiplication(n)`** - Générer la table de multiplication
4. **`trouver_maximum(nums)`** - Trouver la valeur maximale
5. **`calculer_moyenne(nums)`** - Calculer la moyenne
6. **`compter_negatifs(nums)`** - Compter les nombres négatifs
7. **`compter_mots(phrase)`** - Compter les mots d'une phrase
8. **`trouver_plus_long(items)`** - Trouver le mot le plus long
9. **`convertir_majuscule(items)`** - Convertir en majuscules
10. **`compter_mots_commencant_par(items, lettre)`** - Compter mots commençant par une lettre
11. **`trouver_mot_finissant_par(items, suffixe)`** - Trouver mots finissant par un suffixe
12. **`compter_caracteres(s, char)`** - Compter occurrences d'un caractère
13. **`inverser_chaine(s)`** - Inverser une chaîne
14. **`trouver_occurrences_chaine(s, c)`** - Compter occurrences dans une chaîne

### 🔒 Tuples (5 fonctions)
Opérations sur les tuples immuables :
15. **`somme_pairs_tuples(nums)`** - Somme des pairs dans un tuple
16. **`compter_occurrences_tuples(items, valeur)`** - Compter dans un tuple
17. **`table_multiplication_tuples(n)`** - Table de multiplication (tuple)
18. **`trouver_maximum_tuples(nums)`** - Maximum dans un tuple
19. **`calculer_moyenne_tuples(nums)`** - Moyenne d'un tuple

### 🎲 Sets (5 fonctions)
Opérations sur les ensembles (valeurs uniques) :
20. **`somme_pairs_sets(nums)`** - Somme des pairs dans un set
21. **`compter_occurrences_sets(items, valeur)`** - Vérifier présence (set)
22. **`table_multiplication_sets(n)`** - Table de multiplication (set)
23. **`trouver_maximum_sets(nums)`** - Maximum dans un set
24. **`compter_negatifs_sets(nums)`** - Compter négatifs dans un set

### 📚 Dictionnaires (10 fonctions)
Opérations sur les paires clé-valeur :
25. **`ajouter_element(d, cle, valeur)`** - Ajouter une paire clé-valeur
26. **`supprimer_element(d, cle)`** - Supprimer une clé
27. **`fusionner_dictionnaires(d1, d2)`** - Fusionner deux dictionnaires
28. **`inverser_dictionnaire(d)`** - Échanger clés et valeurs
29. **`compter_valeurs(d)`** - Compter les paires clé-valeur
30. **`trouver_valeur_maximale(d)`** - Trouver la valeur maximale
31. **`trouver_cle_par_valeur(d, valeur)`** - Trouver clés par valeur
32. **`verifier_cle_existe(d, cle)`** - Vérifier existence d'une clé
33. **`valeurs_uniques(d)`** - Extraire valeurs uniques
34. **`mettre_a_jour_valeur(d, cle, nouvelle_valeur)`** - Mettre à jour une valeur

## 🚀 Comment démarrer

1. Ouvrir le fichier `src/exercices.py`
2. Implémenter les fonctions progressivement par catégorie
3. Lancer les tests pour vérifier :
   ```bash
   pytest -q ex02_boucles_listes_dictionaire
   ```

## 💡 Astuces

### Boucles
- **`for item in collection`** : Parcourir les éléments
- **`for i in range(n)`** : Boucle avec compteur
- **Compréhensions de liste** : `[x for x in items if condition]`

### Collections
- **Listes** : Mutables, ordonnées, doublons autorisés → `[]`
- **Tuples** : Immutables, ordonnés, doublons autorisés → `()`
- **Sets** : Mutables, non ordonnés, pas de doublons → `{}`
- **Dictionnaires** : Mutables, paires clé-valeur → `{key: value}`

### Méthodes utiles
- Listes : `.append()`, `.extend()`, `.remove()`, `.pop()`
- Strings : `.split()`, `.upper()`, `.lower()`, `.startswith()`, `.endswith()`
- Dictionnaires : `.keys()`, `.values()`, `.items()`, `.get()`, `.update()`
- Sets : `.add()`, `.remove()`, `.union()`, `.intersection()`

## 📚 Ressources

### Boucles
- [Les boucles for et while en Python](https://python.sdv.univ-paris-diderot.fr/05_boucles/)
- [Compréhensions de liste (List comprehensions)](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7293916-utilisez-des-listes-et-des-tuples)

### Listes et Tuples
- [Listes Python (Documentation officielle)](https://docs.python.org/fr/3/tutorial/datastructures.html)
- [Différence entre listes et tuples](https://realpython.com/python-lists-tuples/)

### Sets
- [Ensembles en Python](https://docs.python.org/fr/3/tutorial/datastructures.html#sets)
- [Guide des sets (Real Python)](https://realpython.com/python-sets/)

### Dictionnaires
- [Dictionnaires Python (Documentation officielle)](https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries)
- [Guide complet des dictionnaires](https://realpython.com/python-dicts/)

### Méthodes de chaînes
- [Méthodes des chaînes de caractères](https://docs.python.org/fr/3/library/stdtypes.html#string-methods)

## ✅ Critères de réussite

- Tous les tests passent (34 tests)
- Utilisation appropriée de chaque structure de données
- Code idiomatique Python (utilisation des compréhensions quand approprié)
- Gestion correcte des cas limites (listes vides, dictionnaires vides, etc.)
