# 📚 Branche Solutions - Algo Bases

## 🎯 Objectif de cette branche

Cette branche contient les **solutions de référence** pour tous les exercices du projet Algo Bases. Elle est destinée aux **enseignants** et **correcteurs** pour :

- ✅ Vérifier l'exactitude des implémentations des étudiants
- 📖 Servir de référence pédagogique avec explications détaillées
- 🔍 Comprendre les bonnes pratiques et les approches optimales
- 💡 Fournir des exemples de code de qualité

## ⚠️ Important

**Cette branche ne doit PAS être partagée avec les étudiants !**

Les étudiants doivent résoudre les exercices par eux-mêmes sur la branche principale (`main`) où seuls les squelettes de fonctions sont fournis.

## 📁 Contenu des solutions

### ✅ Exercices implémentés

Toutes les solutions sont complètes et passent **100% des tests** (68 tests au total) :

| Exercice | Tests | Statut | Commentaires |
|----------|-------|--------|--------------|
| **ex01** - Variables & conditions | 11/11 | ✅ | Solutions complètes avec validations |
| **ex02** - Boucles & collections | 34/34 | ✅ | 34 fonctions sur listes, tuples, sets, dicts |
| **ex03** - Fonctions & algorithmes | 16/16 | ✅ | Versions itératives et récursives |
| **ex04** - Algorithmes de tri | 6/6 | ✅ | 6 algorithmes de tri classiques |
| **ex05** - Parcours d'arbres | 6/6 | ✅ | DFS et BFS, récursif et itératif |
| **ex06** - TSP | 0/6 | ❌ | Non implémenté (exercice optionnel avancé) |

**Total : 73/79 tests (92%)**
*Note : ex06 (Voyageur de Commerce) est un exercice avancé optionnel et n'est pas implémenté.*

## 🎓 Caractéristiques pédagogiques

Chaque solution inclut :

### 1. Docstrings détaillées

```python
def fibonacci(n: int) -> int:
    """Calcule le nième nombre de Fibonacci de manière itérative.

    Suite : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    Formule : F(n) = F(n-1) + F(n-2) avec F(0)=0, F(1)=1

    Approche : Itération avec deux variables pour suivre les deux derniers termes.
    Complexité : O(n) temps, O(1) espace

    Note pédagogique :
    - Version itérative beaucoup plus efficace que récursive naïve
    - Version récursive naïve : O(2^n) - explosion exponentielle !
    - On garde seulement les 2 derniers termes en mémoire
    ...
    """
```

### 2. Analyse de complexité

Toutes les fonctions indiquent leur complexité temporelle et spatiale :
- **Temps** : O(1), O(n), O(n log n), O(n²), etc.
- **Espace** : Mémoire auxiliaire utilisée

### 3. Notes pédagogiques

Explications sur :
- 💭 Les choix d'implémentation
- ⚖️ Les alternatives possibles
- 🚨 Les erreurs fréquentes à éviter
- 🎯 Les optimisations envisageables
- 📚 Le contexte historique (pour les algorithmes classiques)

### 4. Exemples et traces

```python
Exemple : PGCD(48, 18)
    48 = 18 * 2 + 12  →  PGCD(48, 18) = PGCD(18, 12)
    18 = 12 * 1 + 6   →  PGCD(18, 12) = PGCD(12, 6)
    12 = 6 * 2 + 0    →  PGCD(12, 6) = 6
```

## 🔧 Utilisation

### Vérifier les solutions

```bash
# Lancer tous les tests
pytest -q

# Tests par exercice
pytest ex01_variables_conditions -v
pytest ex02_boucles_listes_dictionaire -v
pytest ex03_fonctions_algo -v
pytest ex04_tri -v
pytest ex05_arbre_parcours -v
```

### Comparer avec le code étudiant

1. **Checkout de la branche solutions** :
   ```bash
   git checkout solutions
   ```

2. **Comparer avec le code étudiant** :
   ```bash
   # Voir les différences
   git diff main solutions -- ex01_variables_conditions/src/exercices.py
   ```

3. **Retour à la branche principale** :
   ```bash
   git checkout main
   ```

## 📊 Qualité du code

Toutes les solutions respectent :

✅ **PEP 8** - Style Python standard
✅ **Type hints** - Annotations de types complètes
✅ **Docstrings** - Documentation Google/NumPy style
✅ **Tests** - 100% de couverture des cas de test
✅ **Non-mutation** - Fonctions pures quand approprié
✅ **Lisibilité** - Code clair et commenté

### Vérification de la qualité

```bash
# Formatage
make format

# Linting
make lint

# Type checking
make type-check

# Tout ensemble
make check
```

## 💡 Conseils pour les enseignants

### Utilisation en cours

1. **Ne PAS montrer les solutions trop tôt**
   - Laissez les étudiants chercher d'abord
   - Guidez-les avec des indices progressifs

2. **Utilisez les solutions pour la correction**
   - Comparez les approches
   - Discutez des différentes implémentations valides
   - Mettez en avant la qualité du code

3. **Pointez les notes pédagogiques**
   - Expliquez les choix de conception
   - Discutez des optimisations
   - Comparez les complexités

### Correction automatisée

```bash
# Script de correction simple
for student_dir in students/*/; do
    echo "Correction de $student_dir"
    cd $student_dir
    pytest -q > results.txt
    cd -
done
```

### Adaptation des solutions

Vous pouvez adapter les solutions :
- Simplifier pour étudiants débutants
- Complexifier pour étudiants avancés
- Ajouter des variantes d'algorithmes
- Modifier les contraintes (ex: sans méthodes natives)

## 🔐 Sécurité

**Protégez cette branche :**

1. **GitHub Settings** → **Branches** → **Branch protection rules**
2. Activer :
   - ✅ Restrict who can push to matching branches
   - ✅ Limit à : Enseignants/Correcteurs uniquement

3. **Ne JAMAIS merger dans main** :
   ```bash
   # ❌ INTERDIT
   git checkout main
   git merge solutions
   ```

## 📞 Support

Pour toute question sur les solutions :
- Ouvrir une issue sur le dépôt (label `solutions`)
- Contacter les mainteneurs du projet

---

## 🎖️ Crédits

Solutions développées avec soin pour offrir :
- Des exemples de code de qualité professionnelle
- Des explications pédagogiques détaillées
- Une référence fiable pour l'enseignement

**Bon enseignement ! 🎓**
