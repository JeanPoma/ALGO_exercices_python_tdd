# 🎓 Projet d'algorithmie – Apprentissage par TDD

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-74%20tests-green.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)]()

**Un parcours progressif d'apprentissage de l'algorithmique en Python avec approche TDD (Test-Driven Development)**

Ce projet propose une série d'exercices de programmation structurés en 7 modules, allant des bases (variables, conditions) aux algorithmes avancés (TSP, parcours d'arbres). Chaque exercice est accompagné de tests unitaires qui guident l'apprentissage et valident la progression.

## 📚 Table des matières

- [Vue d'ensemble](#-vue-densemble-des-exercices)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Structure du projet](#-structure-du-projet)
- [Philosophie TDD](#-philosophie-tdd)
- [Benchmarks](#-benchmarks-de-performance)

## 🗺️ Vue d'ensemble des exercices

| Exercice | Titre | Niveau | Temps | Tests | Concepts clés |
|----------|-------|--------|-------|-------|---------------|
| **01** | Variables & conditions | ⭐ | 30-45min | 11 | Types, conditions, exceptions |
| **02** | Boucles, listes & dictionnaires | ⭐⭐ | 1h30-2h | 34 | Boucles, collections, itération |
| **03** | Fonctions & algorithmes célèbres | ⭐⭐⭐ | 2h-3h | 16 | PGCD, Fibonacci, récursivité |
| **04** | Algorithmes de tri | ⭐⭐⭐⭐ | 2h-3h | 6 | Tri insertion, sélection, rapide |
| **05** | Parcours d'arbres | ⭐⭐⭐⭐ | 2h-2h30 | 6 | DFS, BFS, arbres binaires |
| **06** | Voyageur de commerce (TSP) | ⭐⭐⭐⭐⭐ | 3h-4h | 6 | NP-complet, optimisation |
| **07** | Mini-projet Labyrinthe | 🎮 | Variable | - | Projet Pygame guidé |

**Total : 74 tests unitaires + 1 projet guidé**

## 🔧 Prérequis

- **Python 3.10+** ([télécharger](https://www.python.org/downloads/))
- **pip** (gestionnaire de paquets Python)
- Un éditeur de code (VS Code, PyCharm, etc.)
- Connaissances de base en programmation (recommandé mais pas obligatoire)

## 📥 Installation

1. **Cloner le repository** (ou télécharger le ZIP)
   ```bash
   git clone <url-du-repo>
   cd algo_bases
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv .venv
   ```

3. **Activer l'environnement virtuel**
   ```bash
   # Windows
   .venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Utilisation

### Lancer tous les tests

```bash
pytest -q
```

### Lancer les tests d'un exercice spécifique

```bash
# Exercice 01
pytest -q ex01_variables_conditions

# Exercice 02
pytest -q ex02_boucles_listes_dictionaire

# etc.
```

### Workflow recommandé

1. **Lire le README** de l'exercice (ex: `ex01_variables_conditions/README.md`)
2. **Ouvrir le fichier source** (ex: `ex01_variables_conditions/src/exercices.py`)
3. **Implémenter les fonctions** en remplaçant `raise NotImplementedError`
4. **Lancer les tests** pour valider votre code
5. **Itérer** jusqu'à ce que tous les tests passent ✅

## 📁 Structure du projet

```
algo_bases/
├── ex01_variables_conditions/     # Variables, conditions, exceptions
│   ├── src/exercices.py           # Code à compléter
│   ├── tests/test_exercices.py    # Tests unitaires
│   └── README.md                  # Guide de l'exercice
├── ex02_boucles_listes_dictionaire/
├── ex03_fonctions_algo/
├── ex04_tri/
├── ex05_arbre_parcours/
├── ex06_voyageur_commerce/
├── ex07_mini_projet/              # Projet Pygame labyrinthe
├── common/                        # Classes réutilisables
│   └── tree.py                    # Structure d'arbre binaire
├── tools/                         # Outils de benchmark
│   ├── generate_datasets.py       # Génération jeux de données
│   ├── bench_tri.py              # Benchmark des tris
│   └── metrics.py                # Mesures de performance
├── data/                         # Jeux de données pour benchmarks
├── pyproject.toml               # Configuration pytest
├── requirements.txt             # Dépendances Python
└── README.md                    # Ce fichier
```

## 🧪 Philosophie TDD

Ce projet suit une approche **TDD (Test-Driven Development)** :

1. **Red** 🔴 : Les tests échouent car les fonctions ne sont pas implémentées
2. **Green** 🟢 : Vous écrivez le code minimal pour faire passer les tests
3. **Refactor** ♻️ : Vous améliorez le code tout en gardant les tests verts

### Avantages du TDD

- ✅ **Validation immédiate** : Vous savez instantanément si votre code fonctionne
- 🎯 **Objectifs clairs** : Les tests définissent exactement ce qui est attendu
- 🛡️ **Non-régression** : Les tests empêchent d'introduire des bugs
- 📚 **Documentation vivante** : Les tests montrent comment utiliser les fonctions

## 📊 Benchmarks de performance

### Générer les jeux de données

```bash
python tools/generate_datasets.py
```

Crée des fichiers dans `data/` avec différentes caractéristiques :
- Données aléatoires
- Données triées
- Données inversées
- Données presque triées
- Données avec peu de valeurs uniques

### Lancer les benchmarks (tris)

```bash
python tools/bench_tri.py
```

**Résultats** :
- `out/bench_results.csv` : Tableau détaillé des mesures (temps, comparaisons)
- `out/bench_plot.png` : Graphique comparatif (si matplotlib installé)

### Mesurer le temps d'exécution

```python
from tools.measure_time import measure_execution_time

duration = measure_execution_time(ma_fonction, arg1, arg2)
print(f"Temps d'exécution : {duration:.4f}s")
```

## 🎓 Pour les enseignants

Ce projet peut être utilisé comme :
- Support de cours d'algorithmique
- Travaux pratiques auto-corrigés
- Base pour des projets étudiants
- Exercices de révision avant examens

### 📚 Documentation enseignant

Des ressources complètes sont disponibles pour vous aider :

- **[📖 Guide enseignant](docs/guide_enseignant.md)** - Conseils pédagogiques détaillés par exercice
  - Progression recommandée (semestre ou intensif)
  - Points d'attention et erreurs fréquentes
  - Activités suggérées et différenciation
  - FAQ enseignants

- **[📊 Grille d'évaluation](docs/grille_evaluation.md)** - Barème détaillé et critères
  - Notation par exercice (/10)
  - Critères de qualité du code
  - Bonus et malus
  - Conseils pour la correction

### Personnalisation

- Modifier les tests pour ajuster la difficulté
- Ajouter de nouveaux exercices en suivant la structure existante
- Créer des branches avec solutions pour correction automatique
- Utiliser GitHub Classroom pour gestion automatisée

## 🤝 Contribution

Les contributions sont bienvenues ! Que vous souhaitiez :
- 🐛 Corriger des bugs
- ✨ Ajouter de nouvelles fonctionnalités
- 📚 Améliorer la documentation
- 🎓 Créer de nouveaux exercices
- 🔧 Optimiser les outils existants

**Consultez le [Guide de contribution](CONTRIBUTING.md)** pour :
- Standards de code à respecter
- Processus de développement
- Comment soumettre une Pull Request
- Code de conduite

### Contribution rapide

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Faire vos modifications (`make check-fix && make test`)
4. Commit les changements (`git commit -m 'feat: Description'`)
5. Push vers la branche (`git push origin feature/amelioration`)
6. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🙏 Remerciements

Merci aux contributeurs et à la communauté Python pour les ressources pédagogiques.
