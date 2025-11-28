# 📊 Grille d'évaluation - Algo Bases

## 🎯 Vue d'ensemble

Cette grille d'évaluation fournit un cadre détaillé pour noter les exercices du projet Algo Bases. Elle peut être adaptée selon vos besoins pédagogiques.

---

## 📋 Barème global (sur 20)

| Exercice | Points | Coefficient | Note /20 |
|----------|--------|-------------|----------|
| ex01 - Variables & conditions | /10 | 0.2 | /2 |
| ex02 - Boucles & collections | /10 | 0.3 | /3 |
| ex03 - Fonctions & algorithmes | /10 | 0.4 | /4 |
| ex04 - Algorithmes de tri | /10 | 0.3 | /3 |
| ex05 - Parcours d'arbres | /10 | 0.3 | /3 |
| ex06 - TSP (optionnel/bonus) | /10 | 0.2 | /2 |
| ex07 - Mini-projet | /10 | 0.3 | /3 |
| **TOTAL** | - | - | **/20** |

---

## 📝 Grille détaillée par exercice

### ex01 : Variables & conditions (/10)

#### Tests fonctionnels (/6)
- ✅ Tous les tests passent : **6/6**
- ⚠️ 90-99% des tests passent : **5/6**
- ⚠️ 75-89% des tests passent : **4/6**
- ⚠️ 50-74% des tests passent : **2/6**
- ❌ < 50% des tests passent : **0/6**

#### Qualité du code (/3)
- **Lisibilité** (1 pt)
  - Noms de variables explicites
  - Indentation correcte
  - Pas de code dupliqué
- **Robustesse** (1 pt)
  - Gestion des cas limites
  - Validation des entrées
  - Exceptions appropriées
- **Style PEP 8** (1 pt)
  - Respect des conventions Python
  - Pas de warnings du linter

#### Documentation (/1)
- Commentaires pertinents si nécessaire
- Docstrings présentes (optionnel pour ex01)

**Bonus (+1)** : Implémentation particulièrement élégante ou optimisée

---

### ex02 : Boucles, listes & dictionnaires (/10)

#### Tests fonctionnels (/6)
- Mêmes critères que ex01

#### Qualité du code (/3)
- **Choix des structures de données** (1 pt)
  - Utilisation appropriée listes/tuples/sets/dicts
  - Compréhension de la mutabilité
- **Efficacité des boucles** (1 pt)
  - Pas de boucles inutiles
  - Utilisation de méthodes natives quand approprié
- **Style Python** (1 pt)
  - Utilisation des compréhensions (quand pertinent)
  - Code idiomatique Python

#### Documentation (/1)
- Commentaires explicatifs pour logique complexe

**Malus (-1 à -2)** :
- Modification d'une liste pendant l'itération
- Copie superficielle au lieu de profonde
- Inefficacité majeure (O(n²) au lieu de O(n))

---

### ex03 : Fonctions & algorithmes célèbres (/10)

#### Tests fonctionnels (/5)
- ✅ Tous les tests passent : **5/5**
- Décomposition par partie :
  - Fonctions de base (6) : 1.5 pt
  - Algorithmes itératifs (6) : 2 pts
  - Algorithmes récursifs (5) : 1.5 pt

#### Qualité du code (/3)
- **Décomposition fonctionnelle** (1 pt)
  - Fonctions bien découpées
  - Respect du principe de responsabilité unique
- **Algorithmes corrects** (1 pt)
  - Implémentation fidèle aux algorithmes classiques
  - Complexité appropriée
- **Récursivité** (1 pt)
  - Cas de base corrects
  - Appels récursifs appropriés
  - Pas de récursion infinie

#### Compréhension algorithmique (/2)
- Commentaires expliquant la logique
- Choix justifiés (itératif vs récursif)

**Bonus (+1 à +2)** :
- Mémoïsation de Fibonacci récursif
- Analyse de complexité documentée
- Tests de performance comparatifs

---

### ex04 : Algorithmes de tri (/10)

#### Tests fonctionnels (/4)
- Tous les tris fonctionnels : **4/4**
- Par algorithme (chacun sur 0.67 pt) :
  - Tri par insertion
  - Tri par sélection
  - Tri rapide (quicksort)
  - Tri par bulle
  - Tri par tas
  - Tri de Shell

#### Qualité d'implémentation (/3)
- **Non-mutation** (1 pt)
  - Les listes d'entrée ne sont pas modifiées
  - Création de copies appropriées
- **Correctness algorithmique** (1 pt)
  - Implémentation fidèle aux algorithmes
  - Cas limites gérés (liste vide, un élément)
- **Complexité** (1 pt)
  - Complexité attendue respectée
  - Pas d'opérations inutiles

#### Analyse de performance (/3)
- **Benchmarks exécutés** (1 pt)
  - Génération des datasets
  - Exécution de `bench_tri.py`
- **Interprétation** (2 pts)
  - Commentaires sur les résultats
  - Compréhension des différences de performance
  - Identification meilleur/pire cas

**Bonus (+2)** :
- Implémentation d'un tri supplémentaire
- Visualisation des résultats (graphiques)
- Analyse O(n) détaillée par écrit

---

### ex05 : Parcours d'arbres (/10)

#### Tests fonctionnels (/5)
- Tous les parcours fonctionnels : **5/5**
- Par parcours :
  - Préfixe, infixe, suffixe (récursifs) : 2.5 pts
  - DFS, BFS (itératifs) : 2.5 pts

#### Qualité du code (/3)
- **Récursivité** (1 pt)
  - Cas de base (arbre vide)
  - Appels récursifs corrects
- **Structures itératives** (1 pt)
  - Utilisation correcte pile/file
  - Choix de `collections.deque` pour BFS
- **Clarté** (1 pt)
  - Code lisible et bien structuré

#### Compréhension (/2)
- Commentaires expliquant les différences DFS/BFS
- Compréhension de l'ordre de parcours

**Bonus (+1)** :
- Implémentation d'un BST (Binary Search Tree)
- Recherche dans l'arbre
- Visualisation des parcours

---

### ex06 : Voyageur de Commerce (optionnel) (/10)

**Note** : Cet exercice peut être noté en bonus ou optionnel.

#### Implémentations (/6)
- **Utilitaires** (1 pt)
  - Génération de villes
  - Calcul de distance
- **Brute force** (2 pts)
  - Toutes les permutations
  - Solution optimale trouvée
- **Greedy** (1 pt)
  - Plus proche voisin
  - Solution approximative
- **DP ou Génétique** (2 pts)
  - Au moins une approche avancée

#### Analyse (/4)
- **Complexité** (2 pts)
  - Compréhension de l'explosion combinatoire
  - Analyse des différentes approches
- **Mesures** (2 pts)
  - Comparaison des temps d'exécution
  - Comparaison qualité des solutions

**Bonus possible** : +2 à +5 selon l'approfondissement

---

### ex07 : Mini-projet Labyrinthe (/10)

#### Fonctionnalités (/5)
- **Chargement JSON** (1 pt)
  - Lecture et validation
  - Structure de données appropriée
- **Affichage Pygame** (1 pt)
  - Grille correctement affichée
  - Couleurs appropriées
- **Déplacements** (1 pt)
  - Contrôles fonctionnels
  - Collisions gérées
- **Score/HUD** (1 pt)
  - Points collectés
  - Affichage score
- **IA (DFS/BFS)** (1 pt)
  - Au moins un algorithme fonctionnel
  - Résolution automatique

#### Qualité du code (/3)
- **Structure** (1 pt)
  - Code organisé en modules
  - Séparation des responsabilités
- **Robustesse** (1 pt)
  - Gestion des erreurs
  - Pas de crashes
- **Style** (1 pt)
  - Code propre et lisible
  - Respect des conventions

#### Créativité (/2)
- Fonctionnalités bonus
- Interface améliorée
- Nouveaux labyrinthes

**Bonus (+3)** :
- Comparaison temps/longueur DFS vs BFS
- Générateur de labyrinthes
- Mode multijoueur

---

## 🎓 Critères transversaux

### Qualité globale du code (appliqué à tous)

#### Excellent (9-10/10)
- ✅ Tous les tests passent
- ✅ Code propre et bien structuré
- ✅ Documentation claire
- ✅ Pas de warnings linter
- ✅ Gestion complète des cas limites
- ✨ Approche élégante ou optimisée

#### Bien (7-8/10)
- ✅ 90%+ des tests passent
- ✅ Code lisible
- ✅ Structure correcte
- ⚠️ Quelques warnings mineurs
- ✅ Principaux cas limites gérés

#### Satisfaisant (5-6/10)
- ⚠️ 75-90% des tests passent
- ⚠️ Code fonctionnel mais perfectible
- ⚠️ Quelques problèmes de structure
- ⚠️ Documentation limitée

#### Insuffisant (< 5/10)
- ❌ < 75% des tests passent
- ❌ Code difficile à lire
- ❌ Problèmes de conception
- ❌ Pas de gestion des erreurs

---

## 🚫 Malus généraux

| Problème | Malus |
|----------|-------|
| Code ne s'exécute pas | -5 pts |
| Plagiat détecté | 0/20 + sanction |
| Pas de tests du tout | -3 pts |
| Warnings linter nombreux | -1 pt |
| Pas de .gitignore / fichiers cache committé | -0.5 pt |
| Code très mal indenté | -1 pt |
| Hardcoding de valeurs de tests | -2 pts |

---

## ✨ Bonus valorisables

| Réalisation | Bonus |
|-------------|-------|
| Tests supplémentaires créés | +1 pt |
| Documentation exemplaire | +1 pt |
| Optimisation significative | +1 à +2 pts |
| Contribution au projet (PR) | +2 pts |
| Analyse de complexité détaillée | +1 pt |
| Visualisations/graphiques | +1 pt |
| Implémentation d'algorithmes supplémentaires | +2 pts |

**Maximum bonus** : +5 points (peut dépasser 20/20)

---

## 📊 Grille de notation rapide

### Pour correction rapide

```
[ ] Tests : ___ / 6
[ ] Code : ___ / 3
[ ] Doc : ___ / 1
[ ] Bonus : ___
Total : ___ / 10
```

### Checklist qualité

- [ ] Le code s'exécute sans erreur
- [ ] Les tests passent (au moins 75%)
- [ ] Les noms de variables sont explicites
- [ ] Le code est indenté correctement
- [ ] Les cas limites sont gérés
- [ ] Pas de code dupliqué
- [ ] Pas de warnings majeurs
- [ ] Documentation minimale présente

---

## 💡 Conseils pour la notation

### Soyez cohérent
- Utilisez la même grille pour tous les étudiants
- Notez par "vagues" (tous les ex01, puis tous les ex02, etc.)

### Donnez du feedback
- Commentaires constructifs
- Points forts et axes d'amélioration
- Encouragement pour les efforts

### Utilisez les outils
```bash
# Vérifier les tests
make test-ex01

# Vérifier la qualité
make check

# Voir la couverture
make test-cov
```

### Détection de plagiat
- Utiliser MOSS ou JPlag
- Comparer les approches (pas seulement le code)
- Oral de soutenance recommandé

---

## 📞 Questions fréquentes

**Q : Comment gérer les retards ?**
R : Suggéré : -1 pt par jour de retard (max -5 pts)

**Q : Accepter le travail en binôme ?**
R : Oui pour ex07, individuel pour ex01-ex06

**Q : Combien de temps prévoir pour corriger ?**
R : ~15-20 min par étudiant avec les outils automatisés

**Q : Faut-il noter le style de code ?**
R : Oui, 15-25% de la note selon la grille. Utilisez `make lint`.

---

## 🔄 Adaptation de la grille

Cette grille est un **modèle**. Adaptez-la selon :
- Votre niveau d'enseignement (L1, L2, L3...)
- Le temps disponible
- Les objectifs pédagogiques spécifiques
- Le contexte (cours, TP, projet personnel)

**N'hésitez pas à ajuster les coefficients et critères !**
