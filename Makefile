.PHONY: help install install-dev test lint format format-check type-check check clean benchmark

# Variables
PYTHON := python
PYTEST := pytest
RUFF := ruff
BLACK := black
MYPY := mypy

# Couleurs pour l'affichage
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Afficher ce message d'aide
	@echo "$(BLUE)Commandes disponibles :$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

install: ## Installer les dépendances de base
	@echo "$(BLUE)Installation des dépendances...$(NC)"
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e .

install-dev: ## Installer les dépendances de développement
	@echo "$(BLUE)Installation des dépendances de développement...$(NC)"
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e ".[dev]"

test: ## Lancer tous les tests
	@echo "$(BLUE)Lancement des tests...$(NC)"
	$(PYTEST) -v

test-fast: ## Lancer les tests en mode rapide (sans verbose)
	@echo "$(BLUE)Lancement des tests rapides...$(NC)"
	$(PYTEST) -q

test-cov: ## Lancer les tests avec couverture de code
	@echo "$(BLUE)Lancement des tests avec couverture...$(NC)"
	$(PYTEST) --cov=. --cov-report=term-missing --cov-report=html

lint: ## Vérifier le code avec ruff
	@echo "$(BLUE)Vérification du code avec ruff...$(NC)"
	$(RUFF) check .

lint-fix: ## Corriger automatiquement les problèmes détectés par ruff
	@echo "$(BLUE)Correction automatique avec ruff...$(NC)"
	$(RUFF) check --fix .

format: ## Formater le code avec black
	@echo "$(BLUE)Formatage du code avec black...$(NC)"
	$(BLACK) .

format-check: ## Vérifier le formatage sans modifier les fichiers
	@echo "$(BLUE)Vérification du formatage...$(NC)"
	$(BLACK) --check --diff .

type-check: ## Vérifier les types avec mypy
	@echo "$(BLUE)Vérification des types avec mypy...$(NC)"
	$(MYPY) . || true

check: lint format-check type-check ## Lancer toutes les vérifications (lint + format + types)
	@echo "$(GREEN)✓ Toutes les vérifications sont terminées$(NC)"

check-fix: lint-fix format ## Corriger automatiquement tous les problèmes
	@echo "$(GREEN)✓ Code corrigé et formaté$(NC)"

clean: ## Nettoyer les fichiers temporaires
	@echo "$(BLUE)Nettoyage...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type f -name "*.coverage" -delete 2>/dev/null || true
	rm -rf htmlcov/ 2>/dev/null || true
	rm -rf out/*.csv out/*.png 2>/dev/null || true
	@echo "$(GREEN)✓ Nettoyage terminé$(NC)"

benchmark: ## Générer les datasets et lancer les benchmarks de tri
	@echo "$(BLUE)Génération des datasets...$(NC)"
	$(PYTHON) tools/generate_datasets.py
	@echo "$(BLUE)Lancement des benchmarks...$(NC)"
	$(PYTHON) tools/bench_tri.py

ci: check test ## Simulation CI/CD locale (vérifications + tests)
	@echo "$(GREEN)✓ CI simulée avec succès$(NC)"

# Commandes pour les exercices individuels
test-ex01: ## Tester uniquement l'exercice 01
	$(PYTEST) -v ex01_variables_conditions

test-ex02: ## Tester uniquement l'exercice 02
	$(PYTEST) -v ex02_boucles_listes_dictionaire

test-ex03: ## Tester uniquement l'exercice 03
	$(PYTEST) -v ex03_fonctions_algo

test-ex04: ## Tester uniquement l'exercice 04
	$(PYTEST) -v ex04_tri

test-ex05: ## Tester uniquement l'exercice 05
	$(PYTEST) -v ex05_arbre_parcours

test-ex06: ## Tester uniquement l'exercice 06
	$(PYTEST) -v ex06_voyageur_commerce
