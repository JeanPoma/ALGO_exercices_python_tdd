# 📚 Guide Enseignant - Algo Bases

## 🎯 Vue d'ensemble

Ce guide est destiné aux enseignants utilisant ce projet pour leurs cours d'algorithmique et de programmation en Python. Il fournit des conseils pédagogiques, des suggestions de progression, et des points d'attention pour chaque exercice.

---

## 📅 Progression pédagogique recommandée

### Semestre type (12 semaines)

| Semaine | Exercice | Séances | Objectifs pédagogiques |
|---------|----------|---------|------------------------|
| 1-2 | ex01 | 2 × 2h | Bases Python, variables, conditions |
| 3-4 | ex02 | 2 × 2h | Collections Python, boucles |
| 5-7 | ex03 | 3 × 2h | Fonctions, algorithmes classiques, récursivité |
| 8-9 | ex04 | 2 × 2h | Algorithmes de tri, analyse de complexité |
| 10 | ex05 | 1 × 2h | Structures d'arbres, parcours |
| 11 | ex06 | 1 × 2h | Optimisation, NP-complet |
| 12 | ex07 | 1 × 2h | Projet intégrateur |

### Format intensif (4 semaines)

| Semaine | Contenu | Charge |
|---------|---------|--------|
| 1 | ex01 + ex02 | 8-10h |
| 2 | ex03 + ex04 | 10-12h |
| 3 | ex05 + ex06 | 8-10h |
| 4 | ex07 + révisions | 6-8h |

---

## 📖 Guide par exercice

### ex01 : Variables & conditions ⭐

**Objectifs pédagogiques :**
- Introduction à Python et à l'environnement de développement
- Compréhension des types de base
- Maîtrise des structures conditionnelles

**Points d'attention :**
- ⚠️ **Année bissextile** : Beaucoup d'étudiants oublient la règle des multiples de 400
- ⚠️ **Calcul de réduction** : Pensez à valider les entrées négatives
- ⚠️ **Conversion binaire** : Certains essaient d'utiliser `bin()` directement (encourager l'algorithme)

**Conseils d'enseignement :**
- Commencer par une démonstration en live coding (somme, produit)
- Expliquer la différence entre `=` (affectation) et `==` (comparaison)
- Introduire le débogueur Python (breakpoints)

**Erreurs fréquentes :**
- Oubli du `return` dans les fonctions
- Confusion entre `is` et `==` pour les booléens
- Gestion d'exceptions avec `try/except` au lieu de validation

**Temps estimé étudiant moyen :** 45-60 minutes

---

### ex02 : Boucles, listes & dictionnaires ⭐⭐

**Objectifs pédagogiques :**
- Maîtrise des structures de données Python
- Compréhension de la mutabilité
- Pratique intensive des boucles

**Points d'attention :**
- ⚠️ **Différences listes/tuples/sets** : Concept clé souvent mal compris
- ⚠️ **Dictionnaires** : Inverser un dictionnaire avec valeurs dupliquées
- ⚠️ **Compréhensions de liste** : Encourager mais ne pas forcer

**Conseils d'enseignement :**
- Faire un tableau comparatif des collections (mutable, ordonné, doublons)
- Démontrer l'impact de la mutabilité avec des exemples concrets
- Montrer les méthodes natives avant de coder "from scratch"

**Erreurs fréquentes :**
- Modifier une liste pendant l'itération
- Confusion entre `.append()` et `.extend()`
- Oubli que les dictionnaires itèrent sur les clés par défaut

**Exercices bonus suggérés :**
- Implémenter un compteur de fréquence de mots
- Créer un index inversé (mot → positions)

**Temps estimé étudiant moyen :** 2-3 heures

---

### ex03 : Fonctions & algorithmes célèbres ⭐⭐⭐

**Objectifs pédagogiques :**
- Décomposition en fonctions
- Algorithmes classiques de l'informatique
- Introduction à la récursivité

**Points d'attention :**
- ⚠️ **Récursivité** : Concept difficile pour débutants
- ⚠️ **PGCD** : Bien expliquer l'algorithme d'Euclide
- ⚠️ **Crible d'Ératosthène** : Complexité de l'algorithme
- ⚠️ **Recherche binaire** : Nécessite liste triée

**Conseils d'enseignement :**
- Faire d'abord les versions itératives
- Expliquer la récursivité avec des schémas (pile d'appels)
- Utiliser un débogueur pour visualiser la récursion
- Comparer performances itératif vs récursif (timeit)

**Erreurs fréquentes :**
- Récursion infinie (oubli du cas de base)
- Fibonacci récursif sans mémoïsation (très lent)
- Recherche binaire avec indices incorrects (off-by-one)

**Activités suggérées :**
- Dessiner l'arbre d'appels de Fibonacci(5)
- Mesurer le temps de crible pour n=10000, 100000, 1000000
- Comparer recherche linéaire vs binaire

**Temps estimé étudiant moyen :** 3-4 heures

---

### ex04 : Algorithmes de tri ⭐⭐⭐⭐

**Objectifs pédagogiques :**
- Comprendre les algorithmes de tri classiques
- Analyser la complexité algorithmique
- Mesurer les performances réelles

**Points d'attention :**
- ⚠️ **Ne pas muter la liste d'entrée** : Créer une copie
- ⚠️ **Tri rapide** : Choix du pivot impacte la performance
- ⚠️ **Stabilité** : Certains tris sont stables, d'autres non

**Conseils d'enseignement :**
- Utiliser des visualisations (animations en ligne)
- Faire trier des cartes à jouer physiquement (tri insertion)
- Comparer les benchmarks sur différents datasets
- Expliquer O(n²) vs O(n log n) avec des graphiques

**Erreurs fréquentes :**
- Tri par insertion avec swap au lieu d'insertion
- Tri rapide qui modifie la liste originale
- Confusion entre tri stable et non-stable

**Activités suggérées :**
- Analyser `bench_results.csv` et interpréter les résultats
- Implémenter un tri "stupide" (bogosort) pour comparaison
- Mesurer le pire cas du tri rapide

**Benchmarks à faire en classe :**
```bash
python tools/generate_datasets.py
python tools/bench_tri.py
```

**Temps estimé étudiant moyen :** 3-4 heures

---

### ex05 : Parcours d'arbres ⭐⭐⭐⭐

**Objectifs pédagogiques :**
- Comprendre les structures arborescentes
- Différencier DFS et BFS
- Implémenter récursion et itération (pile/file)

**Points d'attention :**
- ⚠️ **Arbre vide** : Gérer le cas `None`
- ⚠️ **DFS vs BFS** : Bien faire comprendre la différence
- ⚠️ **Files et piles** : Utiliser `collections.deque` pour efficacité

**Conseils d'enseignement :**
- Dessiner des arbres au tableau
- Faire tracer à la main les différents parcours
- Montrer que BFS trouve le plus court chemin
- Expliquer pile (LIFO) vs file (FIFO)

**Erreurs fréquentes :**
- Oubli de vérifier `if node is not None`
- Confusion entre préfixe/infixe/suffixe
- Utiliser une liste comme file (inefficace)

**Activités suggérées :**
- Créer un arbre binaire de recherche (BST)
- Implémenter une recherche dans l'arbre
- Visualiser les parcours avec des print

**Temps estimé étudiant moyen :** 2-3 heures

---

### ex06 : Voyageur de commerce (TSP) ⭐⭐⭐⭐⭐

**Objectifs pédagogiques :**
- Comprendre les problèmes NP-complets
- Comparer approches exactes et heuristiques
- Introduction aux algorithmes génétiques

**Points d'attention :**
- ⚠️ **Complexité** : Exercice avancé, peut être frustrant
- ⚠️ **Brute force** : Limiter à 8-10 villes max
- ⚠️ **Algorithme génétique** : Concept nouveau pour beaucoup

**Conseils d'enseignement :**
- Bien expliquer P vs NP
- Montrer l'explosion combinatoire (factorielle)
- Accepter des implémentations partielles
- L'algorithme génétique peut être simplifié

**Erreurs fréquentes :**
- Oublier de revenir au point de départ
- Distance asymétrique (ne pas assumer symétrie)
- Algorithme génétique sans critère d'arrêt

**Activités suggérées :**
- Calculer le nombre de permutations pour n villes
- Visualiser les chemins avec matplotlib
- Comparer temps d'exécution des 4 approches

**Note importante :** Cet exercice peut être rendu optionnel ou noté en bonus.

**Temps estimé étudiant moyen :** 4-6 heures

---

### ex07 : Mini-projet Labyrinthe 🎮

**Objectifs pédagogiques :**
- Projet intégrateur (tout ce qui a été vu)
- Gestion d'un projet plus complexe
- Introduction à Pygame

**Conseils d'enseignement :**
- Peut être fait en binôme
- Décomposer en sous-tâches claires
- Code review recommandé

**Évaluation suggérée :**
- Fonctionnalités implémentées (50%)
- Qualité du code (25%)
- Créativité/bonus (25%)

**Temps estimé étudiant moyen :** 6-10 heures

---

## 🎯 Conseils généraux d'enseignement

### Approche TDD

**Avantages pour l'apprentissage :**
- ✅ Feedback immédiat
- ✅ Objectifs clairs
- ✅ Encourage les tests unitaires

**Comment l'enseigner :**
1. Montrer un test qui échoue (Red)
2. Écrire le code minimal qui passe (Green)
3. Améliorer le code (Refactor)

### Utilisation du Makefile

Enseigner aux étudiants :
```bash
make test          # Lancer tous les tests
make test-ex01     # Tester un exercice
make check-fix     # Formater le code
make clean         # Nettoyer
```

### Code Review

**Conseils :**
- Faire des reviews régulières
- Utiliser les GitHub Actions (CI)
- Encourager le pair programming

### Différenciation pédagogique

**Pour les étudiants avancés :**
- Optimiser la complexité
- Implémenter des variantes
- Contribuer de nouveaux exercices

**Pour les étudiants en difficulté :**
- Fournir des indices progressifs (créer `hints.md`)
- Sessions de tutorat
- Réduire le nombre de fonctions obligatoires

---

## 📊 Évaluation

### Barème suggéré (sur 20)

| Exercice | Points | Commentaire |
|----------|--------|-------------|
| ex01 | 2 pts | Bases essentielles |
| ex02 | 3 pts | Collections importantes |
| ex03 | 4 pts | Algorithmes fondamentaux |
| ex04 | 3 pts | Complexité |
| ex05 | 3 pts | Structures avancées |
| ex06 | 2 pts | Bonus/optionnel |
| ex07 | 3 pts | Projet intégrateur |

### Critères de notation

**Par exercice :**
- Tests qui passent : 60%
- Qualité du code : 25%
- Documentation/commentaires : 15%

**Qualité du code :**
- Nommage clair des variables
- Respect de PEP 8 (vérifier avec `make lint`)
- Gestion des cas limites
- Complexité appropriée

---

## 🛠️ Outils pour l'enseignant

### Commandes utiles

```bash
# Voir les résultats des tests
make test-cov

# Vérifier le code des étudiants
make check

# Comparer les performances
python tools/bench_tri.py
```

### GitHub Classroom

Ce projet peut être utilisé avec GitHub Classroom :
1. Créer un template repository
2. Les étudiants forkent automatiquement
3. Les GitHub Actions testent chaque push
4. Vous voyez les résultats centralisés

---

## 💡 FAQ Enseignants

**Q : Combien de temps prévoir pour tout le cours ?**
R : 40-60h de travail étudiant total (cours + TP + autonomie)

**Q : Les solutions sont-elles disponibles ?**
R : Oui, voir la branche `solutions` (à créer)

**Q : Comment éviter la triche entre étudiants ?**
R :
- Utiliser des détecteurs de plagiat (MOSS)
- Varier légèrement les exercices entre groupes
- Oral de soutenance

**Q : Python 3.10+ est obligatoire ?**
R : Oui pour les type hints modernes. Pour Python < 3.10, adapter `from __future__ import annotations`

**Q : Peut-on utiliser ce projet pour un MOOC ?**
R : Oui, licence MIT. Pensez à créditer le projet source.

---

## 📞 Support et Communauté

- Issues GitHub : Signaler bugs ou suggestions
- Discussions : Partager expériences pédagogiques
- Contributions : Pull requests bienvenues

**N'hésitez pas à adapter ce contenu à votre contexte pédagogique !**
