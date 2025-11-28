# 🤝 Guide de contribution - Algo Bases

Merci de votre intérêt pour contribuer à Algo Bases ! Ce guide vous aidera à proposer des améliorations de qualité.

---

## 📋 Table des matières

- [Code de conduite](#-code-de-conduite)
- [Comment contribuer](#-comment-contribuer)
- [Standards de code](#-standards-de-code)
- [Processus de développement](#-processus-de-développement)
- [Types de contributions](#-types-de-contributions)
- [Processus de review](#-processus-de-review)

---

## 📜 Code de conduite

### Nos engagements

Ce projet s'engage à fournir un environnement accueillant et inclusif pour tous, indépendamment de :
- L'âge, l'origine, l'apparence
- Le niveau d'expérience
- L'identité et l'expression de genre
- La nationalité, la race, la religion

### Comportements attendus

- ✅ Utiliser un langage accueillant et inclusif
- ✅ Respecter les points de vue et expériences différents
- ✅ Accepter les critiques constructives avec grâce
- ✅ Se concentrer sur ce qui est meilleur pour la communauté

### Comportements inacceptables

- ❌ Langage ou images sexualisés
- ❌ Trolling, insultes ou commentaires dénigrants
- ❌ Harcèlement public ou privé
- ❌ Publication d'informations privées sans permission

---

## 🚀 Comment contribuer

### Avant de commencer

1. **Vérifiez les issues existantes**
   - Cherchez si votre idée n'existe pas déjà
   - Commentez sur l'issue pour manifester votre intérêt

2. **Créez une issue pour discuter**
   - Grandes fonctionnalités : Créez une issue avant le code
   - Petits bugs : Vous pouvez directement soumettre une PR

3. **Forkez le projet**
   ```bash
   # Cloner votre fork
   git clone https://github.com/VOTRE-USERNAME/algo_bases.git
   cd algo_bases

   # Ajouter l'upstream
   git remote add upstream https://github.com/ORIGINAL/algo_bases.git
   ```

### Workflow de contribution

1. **Créer une branche**
   ```bash
   git checkout -b feature/nom-fonctionnalite
   # ou
   git checkout -b fix/nom-bug
   ```

2. **Faire vos modifications**
   - Respectez les standards de code (voir ci-dessous)
   - Ajoutez des tests si nécessaire
   - Mettez à jour la documentation

3. **Tester localement**
   ```bash
   make install-dev      # Installer les dépendances dev
   make check-fix        # Formater et corriger
   make test             # Lancer les tests
   make ci               # Simuler la CI
   ```

4. **Commiter**
   ```bash
   git add .
   git commit -m "Type: Description courte

   Description plus détaillée si nécessaire.

   Fixes #123"
   ```

5. **Pousser et créer une PR**
   ```bash
   git push origin feature/nom-fonctionnalite
   ```

   Puis créez la Pull Request sur GitHub.

---

## 💻 Standards de code

### Style Python (PEP 8)

- **Line length** : 100 caractères maximum
- **Indentation** : 4 espaces (pas de tabs)
- **Imports** : Groupés et triés (ruff fait ça automatiquement)
- **Nommage** :
  - Variables/fonctions : `snake_case`
  - Classes : `PascalCase`
  - Constantes : `UPPER_CASE`

### Formatage automatique

Le projet utilise **Black** et **Ruff** :

```bash
make format       # Formater avec Black
make lint-fix     # Corriger avec Ruff
make check-fix    # Les deux
```

### Type hints

Utilisez les type hints Python moderne :

```python
from __future__ import annotations

def ma_fonction(param: str, nombre: int = 0) -> list[str]:
    """Docstring explicative."""
    return [param] * nombre
```

### Docstrings

Format Google/NumPy préféré :

```python
def fonction_exemple(param1: str, param2: int) -> bool:
    """
    Courte description sur une ligne.

    Description plus détaillée si nécessaire.

    Args:
        param1: Description du paramètre
        param2: Description du second paramètre

    Returns:
        Description de ce qui est retourné

    Raises:
        ValueError: Quand la valeur est invalide
    """
    pass
```

### Tests

- Tous les nouveaux codes doivent avoir des tests
- Utilisez `pytest`
- Nommage : `test_nom_fonction_cas_teste`

```python
def test_somme_nombres_positifs():
    assert somme(2, 3) == 5

def test_somme_nombres_negatifs():
    assert somme(-2, -3) == -5
```

---

## 🔨 Processus de développement

### Configuration de l'environnement

```bash
# 1. Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# 2. Installer les dépendances de développement
make install-dev

# 3. Vérifier que tout fonctionne
make test
```

### Avant de commiter

Vérifiez toujours :

```bash
# 1. Formater et corriger
make check-fix

# 2. Lancer les tests
make test

# 3. Vérifier les types
make type-check

# 4. Simuler la CI
make ci
```

### Messages de commit

Format recommandé :

```
Type: Titre court (50 caractères max)

Description détaillée (72 caractères par ligne max).
Expliquez le "pourquoi", pas le "quoi".

- Point 1
- Point 2

Fixes #123
Closes #456
```

**Types de commits** :
- `feat`: Nouvelle fonctionnalité
- `fix`: Correction de bug
- `docs`: Documentation uniquement
- `style`: Formatage, pas de changement de code
- `refactor`: Refactoring sans changement de comportement
- `test`: Ajout/modification de tests
- `chore`: Tâches de maintenance

---

## 📝 Types de contributions

### 1. Corrections de bugs 🐛

**Comment signaler un bug :**
1. Vérifier qu'il n'est pas déjà signalé
2. Créer une issue avec :
   - Description claire
   - Steps to reproduce
   - Comportement attendu vs actuel
   - Version Python et OS
   - Stack trace si applicable

**Soumettre un fix :**
- Créer un test qui reproduit le bug
- Fixer le bug
- S'assurer que le test passe
- Référencer l'issue dans le commit

### 2. Nouvelles fonctionnalités ✨

**Avant de coder :**
1. Créer une issue pour discussion
2. Attendre feedback des mainteneurs
3. Discuter de l'approche

**Inclure dans la PR :**
- Code de la fonctionnalité
- Tests unitaires
- Documentation mise à jour
- Exemple d'utilisation si pertinent

### 3. Documentation 📚

Toujours bienvenue !

- Corrections de typos
- Amélioration de clarté
- Ajout d'exemples
- Traductions
- Tutoriels

**Pas besoin d'issue** pour petites corrections de doc.

### 4. Nouveaux exercices 🎓

**Structure à respecter :**

```
exXX_nom_exercice/
├── README.md           # Documentation complète
├── src/
│   ├── __init__.py
│   └── exercices.py    # Fonctions à implémenter
└── tests/
    └── test_*.py       # Tests unitaires
```

**README obligatoire avec :**
- 📋 Informations (niveau, temps, prérequis, objectifs)
- 📝 Description
- 🎯 Fonctions à implémenter
- 🚀 Comment démarrer
- 💡 Astuces
- 📚 Ressources
- ✅ Critères de réussite

### 5. Outils et scripts 🔧

- Scripts de génération
- Outils d'analyse
- Améliorations du Makefile
- GitHub Actions

---

## 🔍 Processus de review

### Ce que nous vérifions

✅ **Fonctionnalité**
- Le code fait ce qu'il est censé faire
- Les tests passent
- Pas de régression

✅ **Qualité**
- Respect des standards de code
- Pas de warnings linter
- Tests appropriés

✅ **Documentation**
- README mis à jour si nécessaire
- Docstrings présentes
- Commentaires pour code complexe

✅ **Impact**
- Pas de breaking changes non documentés
- Performance acceptable
- Compatible Python 3.10+

### Temps de review

- Issues/bugs simples : 1-3 jours
- Nouvelles fonctionnalités : 3-7 jours
- Grandes contributions : 1-2 semaines

### Après la review

Si des changements sont demandés :
1. Ne pas créer de nouvelle PR
2. Faire les modifications sur la même branche
3. Pusher les changements
4. Répondre aux commentaires

---

## 🎨 Guidelines spécifiques

### Exercices pour étudiants

**Considérations pédagogiques :**
- Progression graduelle de difficulté
- Concepts bien expliqués
- Ressources de qualité fournies
- Tests pédagogiques (pas trop nombreux)

**Ne pas :**
- ❌ Exercices trop complexes d'un coup
- ❌ Dépendances externes lourdes
- ❌ Concepts non introduits

### Tests

**Tests doivent être :**
- ✅ Indépendants (pas d'ordre requis)
- ✅ Rapides (< 1s par test idéalement)
- ✅ Déterministes (pas de random sans seed)
- ✅ Descriptifs (nom de test clair)

**Coverage :**
- Minimum 80% pour nouveau code
- Tester les cas limites
- Tester les cas d'erreur

### Documentation

**README d'exercice :**
- Format Markdown bien formaté
- Emojis pour structure (📋, 🎯, etc.)
- Ressources françaises ET anglaises
- Exemples de code si pertinent

---

## ❓ Questions ?

### Où demander de l'aide ?

- **Questions générales** : GitHub Discussions
- **Bugs** : GitHub Issues
- **Contribution spécifique** : Commentaires sur PR

### Ressources utiles

- [Guide Python officiel](https://docs.python.org/fr/3/)
- [PEP 8](https://pep8.org/)
- [pytest documentation](https://docs.pytest.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

---

## 🏆 Contributeurs

Merci à tous les contributeurs ! Votre travail est apprécié. 🙏

Les contributeurs significatifs sont listés dans le README principal.

---

## 📜 Licence

En contribuant, vous acceptez que vos contributions soient sous la même licence MIT que le projet.

---

**Prêt à contribuer ? On a hâte de voir votre travail ! 🚀**
