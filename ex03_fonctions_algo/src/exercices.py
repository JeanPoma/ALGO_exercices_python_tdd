from __future__ import annotations

# Prise en main
# Exemples simples : Création d'une fonction et appel
def print_hello_world() -> None:
    # Une fonction qui affiche "Hello, world!"
    raise NotImplementedError


def reverse_string(param: str) -> str:
    # Une fonction qui renverse une chaîne donnée en entrée.
    raise NotImplementedError


def to_uppercase(param: str) -> str:
    # Une fonction qui transforme une chaîne en majuscules.
    raise NotImplementedError


def count_substring(param: str, sub: str) -> int:
    # Une fonction qui compte le nombre d'occurrences d'une sous-chaîne dans une chaîne.
    raise NotImplementedError


def list_length(param: list[any]) -> int:
    # Une fonction qui retourne le nombre d'éléments dans une liste d'entiers.
    raise NotImplementedError


def max_in_list(param: list[int]) -> int:
    # Une fonction qui retourne le plus grand élément dans une liste d'entiers.
    raise NotImplementedError


# Fonctions classiques
def pgcd(a: int, b: int) -> int:
    # À FAIRE : Calculer le plus grand commun diviseur (PGCD) de deux entiers.
    # Utiliser l'algorithme d'Euclide en itératif.
    # L'algorithme d'Euclide fonctionne en répétant la division euclidienne entre deux nombres a et b :
    # - Tant que b n'est pas nul, remplacer a par b et b par le reste de la division euclidienne de a par b.
    # - Lorsque b devient nul, le PGCD est la valeur actuelle de a.
    # Une division euclidienne consiste à diviser deux nombres entiers a et b (b ≠ 0) pour obtenir un
    # quotient q et un reste r, tels que : a = b * q + r, avec 0 ≤ r < |b|.
    raise NotImplementedError


def fibonacci(n: int) -> int:
    # La suite de Fibonacci est une suite de nombres où chaque terme est la somme des deux termes précédents,
    # en commençant par 0 et 1. Par exemple : 0, 1, 1, 2, 3, 5, 8, ...
    # À FAIRE : Calculer le nième nombre de Fibonacci de manière itérative.
    raise NotImplementedError


def crible_eratosthene(n: int) -> list[int]:
    # À FAIRE : Implémenter le crible d'Ératosthène pour générer tous les nombres premiers jusqu'à n.
    # Étapes :
    # 1. Créer une liste booléenne de taille n+1 initialement à True, où l'indice représente un nombre.
    # 2. Les indices 0 et 1 doivent être marqués comme False (0 et 1 ne sont pas premiers).
    # 3. Parcourir les entiers p de 2 à √n (inclus).
    # 4. Si p est premier (booléen True), alors marquer tous ses multiples (p*p jusqu'à n) comme False.
    # 5. Extraire les indices marqués True dans la liste et les retourner sous forme de liste de nombres premiers.
    raise NotImplementedError


def is_prime(n: int) -> bool:
    # À FAIRE : Vérifier si un nombre est premier à l'aide de vérifications itératives.
    # Instructions détaillées :
    # 1. Si n est inférieur ou égal à 1, retourner False (les nombres <= 1 ne sont pas premiers).
    # 2. Si n est 2 ou 3, retourner True (2 et 3 sont des nombres premiers).
    # 3. Si n est divisible par 2 ou 3, retourner False (les multiples de 2 et 3 ne sont pas premiers).
    # 4. Utiliser une boucle pour tester les divisibilités d'autres nombres potentiels :
    #    - Initialiser un diviseur potentiel à 5.
    #    - Continuer tant que le carré du diviseur est <= n.
    #    - Si n est divisible par le diviseur ou diviseur + 2, retourner False.
    #    - Incrémenter le diviseur de 6 à chaque tour (car les nombres premiers > 3 sont de la forme 6k ± 1).
    # 5. Si aucune des conditions précédentes n'a permis d'établir que n n'est pas premier, retourner True.
    raise NotImplementedError


def is_palindrome(s: str) -> bool:
    # Un palindrome est une chaîne qui se lit de la même manière à l'endroit et à l'envers.
    # À FAIRE : Vérifier si une chaîne donnée est un palindrome en utilisant l'itération.
    raise NotImplementedError


def binary_search(arr: list[int], target: int) -> int:
    # À FAIRE : Implémenter une recherche binaire sur une liste triée pour trouver la valeur cible.
    # Retourner l'indice de la cible si trouvée, sinon retourner -1.
    raise NotImplementedError


# Fonctions récursives
def gcd_recursive(a: int, b: int) -> int:
    # À FAIRE : Calculer le PGCD de deux entiers récursivement en utilisant l'algorithme d'Euclide.
    raise NotImplementedError


def fibonacci_recursive(n: int) -> int:
    # À FAIRE : Calculer le nième nombre de Fibonacci de manière récursive.
    raise NotImplementedError


def is_prime_recursive(n: int, divisor: int = 2) -> bool:
    # À FAIRE : Vérifier si un nombre est premier en utilisant la récursion.
    # Cas de base : n <= 1 n'est pas premier. Pour n > 1, si divisible par divisor, n'est pas premier.
    # Sinon, incrémenter divisor et vérifier récursivement.
    raise NotImplementedError


def is_palindrome_recursive(s: str) -> bool:
    # À FAIRE : Vérifier si une chaîne donnée est un palindrome en utilisant la récursion.
    # Cas de base : Une chaîne de longueur 0 ou 1 est un palindrome.
    # Étape récursive : Comparer le premier et le dernier caractère et vérifier la sous-chaîne.
    raise NotImplementedError


def factorial_recursive(n: int) -> int:
    # À FAIRE : Calculer la factorielle d'un nombre en utilisant la récursion.
    # Cas de base : n == 0 retourne 1. Étape récursive : n * factorial(n-1).
    raise NotImplementedError
