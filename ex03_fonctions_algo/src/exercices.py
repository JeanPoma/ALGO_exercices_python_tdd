from __future__ import annotations


# =============================================================================
# PRISE EN MAIN - Fonctions simples
# =============================================================================


def print_hello_world() -> str:
    """Retourne 'Hello, World!'.

    Note pédagogique : Retourne une chaîne (pas une fonction void).
    """
    return "Hello, World!"


def reverse_string(param: str) -> str:
    """Renverse une chaîne donnée en entrée.

    Approche : Slicing Python avec pas négatif.
    Complexité : O(n)

    Note pédagogique : [::-1] est l'idiome Python pour inverser.
    """
    return param[::-1]


def to_uppercase(param: str) -> str:
    """Transforme une chaîne en majuscules.

    Approche : Méthode native .upper().
    Complexité : O(n)
    """
    return param.upper()


def count_substring(param: str, sub: str) -> int:
    """Compte le nombre d'occurrences d'une sous-chaîne.

    Approche : Méthode native .count().
    Complexité : O(n * m) où n = len(param), m = len(sub)

    Note pédagogique : count() gère les chevauchements correctement.
    """
    return param.count(sub)


def list_length(param: list[any]) -> int:
    """Retourne le nombre d'éléments dans une liste.

    Approche : Fonction native len().
    Complexité : O(1)

    Note pédagogique : len() fonctionne sur toutes les collections.
    """
    return len(param)


def max_in_list(param: list[int]) -> int:
    """Retourne le plus grand élément dans une liste.

    Approche : Fonction native max().
    Complexité : O(n)

    Note pédagogique : max() parcourt la liste une fois.
    """
    return max(param)


# =============================================================================
# ALGORITHMES CLASSIQUES - Versions itératives
# =============================================================================


def pgcd(a: int, b: int) -> int:
    """Calcule le PGCD (Plus Grand Commun Diviseur) de deux entiers.

    Approche : Algorithme d'Euclide itératif.
    L'algorithme repose sur le principe : PGCD(a, b) = PGCD(b, a mod b)
    On répète jusqu'à ce que b = 0, auquel cas PGCD = a.

    Complexité : O(log(min(a, b)))

    Note pédagogique :
    - Algorithme vieux de 2300 ans (Euclide, -300 av. J.-C.)
    - Très efficace grâce à la propriété mathématique
    - Le reste diminue rapidement (au moins de moitié tous les 2 tours)

    Exemple : PGCD(48, 18)
        48 = 18 * 2 + 12  →  PGCD(48, 18) = PGCD(18, 12)
        18 = 12 * 1 + 6   →  PGCD(18, 12) = PGCD(12, 6)
        12 = 6 * 2 + 0    →  PGCD(12, 6) = 6
    """
    while b != 0:
        a, b = b, a % b
    return a


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

    Exemple : F(5) = 5
        a=0, b=1  (F0=0, F1=1)
        a=1, b=1  (F2=1)
        a=1, b=2  (F3=2)
        a=2, b=3  (F4=3)
        a=3, b=5  (F5=5)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def crible_eratosthene(n: int) -> list[int]:
    """Génère tous les nombres premiers jusqu'à n (inclus).

    Approche : Crible d'Ératosthène - algorithme antique efficace.
    Principe : Marquer tous les multiples de chaque nombre premier.

    Algorithme :
    1. Créer une liste booléenne [True] * (n+1)
    2. Marquer 0 et 1 comme non premiers
    3. Pour chaque p de 2 à √n :
       - Si p est premier, marquer tous ses multiples (p², p²+p, ...) comme composés
    4. Collecter les indices qui restent True

    Complexité : O(n log log n) - très efficace !

    Note pédagogique :
    - On commence à marquer à p² (car les multiples < p² ont déjà été marqués)
    - Optimisation importante : on s'arrête à √n car tout nombre composé ≤ n
      a nécessairement un diviseur ≤ √n
    - Algorithme grec ancien (~200 av. J.-C.) toujours utilisé aujourd'hui

    Exemple : crible_eratosthene(10) -> [2, 3, 5, 7]
    """
    if n < 2:
        return []

    # Initialisation : tous True sauf 0 et 1
    est_premier = [True] * (n + 1)
    est_premier[0] = est_premier[1] = False

    # Marquer les multiples de chaque nombre premier
    p = 2
    while p * p <= n:
        if est_premier[p]:
            # Marquer tous les multiples de p à partir de p²
            for multiple in range(p * p, n + 1, p):
                est_premier[multiple] = False
        p += 1

    # Collecter les nombres premiers
    return [i for i in range(n + 1) if est_premier[i]]


def is_prime(n: int) -> bool:
    """Vérifie si un nombre est premier.

    Approche : Test de divisibilité optimisé.
    Un nombre est premier s'il n'est divisible que par 1 et lui-même.

    Algorithme :
    1. Cas particuliers : n ≤ 1 (non premier), n = 2 ou 3 (premier)
    2. Éliminer multiples de 2 et 3
    3. Tester uniquement les nombres de forme 6k ± 1 jusqu'à √n

    Complexité : O(√n)

    Note pédagogique :
    - Tous les nombres premiers > 3 sont de forme 6k ± 1
      (car 6k, 6k+2, 6k+4 sont pairs ; 6k+3 est divisible par 3)
    - On teste jusqu'à √n car si n = a × b et a > √n, alors b < √n
    - Version simple : tester tous les diviseurs de 2 à √n
    - Version optimisée : tester seulement 2, 3, puis 6k ± 1

    Exemple : is_prime(17) -> True
        17 n'est pas divisible par 2, 3, 5 (√17 ≈ 4.1)
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Tester les nombres de forme 6k ± 1 jusqu'à √n
    divisor = 5
    while divisor * divisor <= n:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6

    return True


def is_palindrome(s: str) -> bool:
    """Vérifie si une chaîne est un palindrome.

    Un palindrome se lit identiquement de gauche à droite et de droite à gauche.

    Approche : Normaliser la chaîne (supprimer espaces, mettre en minuscules),
    puis comparer avec son inverse.
    Complexité : O(n)

    Note pédagogique :
    - On ignore les espaces et la casse
    - "A man a plan a canal Panama" → "amanaplanacanalpanama" → palindrome
    - Étapes : 1) enlever espaces, 2) minuscules, 3) comparer avec inverse

    Alternative avec deux pointeurs (plus efficace) :
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    """
    # Normaliser : enlever espaces et mettre en minuscules
    normalized = s.replace(" ", "").lower()
    return normalized == normalized[::-1]


def binary_search(arr: list[int], target: int) -> int:
    """Recherche binaire sur une liste triée.

    Approche : Algorithme diviser pour régner.
    À chaque étape, on divise l'espace de recherche par 2.

    Prérequis : La liste doit être triée !

    Algorithme :
    1. Définir left=0, right=len(arr)-1
    2. Tant que left ≤ right :
       - Calculer mid = (left + right) // 2
       - Si arr[mid] == target : trouvé, retourner mid
       - Si arr[mid] < target : chercher dans moitié droite (left = mid + 1)
       - Sinon : chercher dans moitié gauche (right = mid - 1)
    3. Si non trouvé : retourner -1

    Complexité : O(log n) - très efficace !

    Note pédagogique :
    - 10x plus rapide que recherche linéaire pour n=1000
    - Pour n=1000000 : ~20 comparaisons vs 1000000 en linéaire
    - Nécessite liste triée (coût du tri : O(n log n))

    Exemple : binary_search([1, 3, 5, 7, 9], 5) -> 2
        [1, 3, 5, 7, 9]  mid=2, arr[2]=5 -> trouvé !
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# =============================================================================
# ALGORITHMES RÉCURSIFS
# =============================================================================


def gcd_recursive(a: int, b: int) -> int:
    """Calcule le PGCD de manière récursive (algorithme d'Euclide).

    Approche : Récursion basée sur PGCD(a, b) = PGCD(b, a mod b).
    Cas de base : b = 0 → PGCD = a

    Complexité : O(log(min(a, b)))

    Note pédagogique :
    - Version récursive plus élégante que l'itérative
    - Chaque appel récursif réduit le problème
    - Terminaison garantie car b diminue strictement

    Exemple : gcd_recursive(48, 18)
        gcd_recursive(48, 18)
         → gcd_recursive(18, 12)
          → gcd_recursive(12, 6)
           → gcd_recursive(6, 0)
            → retourne 6
    """
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def fibonacci_recursive(n: int) -> int:
    """Calcule le nième nombre de Fibonacci de manière récursive.

    Approche : Récursion directe sur la définition F(n) = F(n-1) + F(n-2).
    Cas de base : F(0) = 0, F(1) = 1

    Complexité : O(2^n) - TRÈS INEFFICACE !

    Note pédagogique :
    - Version naïve à but pédagogique UNIQUEMENT
    - Explosion exponentielle : F(40) prend plusieurs secondes !
    - Problème : recalcule les mêmes valeurs des millions de fois
    - Solution : mémoïsation (cache des résultats) ou version itérative

    Arbre d'appels pour F(5) :
                        F(5)
                    /          \\
                F(4)              F(3)
              /     \\          /     \\
          F(3)     F(2)      F(2)    F(1)
         /   \\    /   \\     /   \\
      F(2)  F(1) F(1) F(0) F(1) F(0)
      / \\
    F(1) F(0)

    → F(3) calculé 2 fois, F(2) calculé 3 fois, F(1) calculé 5 fois !
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def is_prime_recursive(n: int, divisor: int = 2) -> bool:
    """Vérifie si un nombre est premier de manière récursive.

    Approche : Test récursif de divisibilité.
    On teste si n est divisible par divisor, puis divisor+1, etc.

    Cas de base :
    - n ≤ 1 : non premier
    - divisor² > n : premier (aucun diviseur trouvé)
    - n % divisor == 0 : non premier (diviseur trouvé)

    Complexité : O(√n)

    Note pédagogique :
    - Version récursive moins naturelle que l'itérative pour ce problème
    - On pourrait optimiser en sautant les pairs après 2
    - Limite de récursion Python : ~1000 appels (problème pour grands n)

    Exemple : is_prime_recursive(17, 2)
        17 % 2 != 0 → is_prime_recursive(17, 3)
        17 % 3 != 0 → is_prime_recursive(17, 4)
        17 % 4 != 0 → is_prime_recursive(17, 5)
        5² > 17 → retourne True
    """
    # Cas de base
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False

    # Appel récursif avec divisor suivant
    return is_prime_recursive(n, divisor + 1)


def is_palindrome_recursive(s: str) -> bool:
    """Vérifie si une chaîne est un palindrome de manière récursive.

    Approche : Comparer premier et dernier caractère, puis récursion sur le milieu.

    Cas de base :
    - Chaîne vide ou 1 caractère : palindrome
    - Premier != dernier : pas palindrome
    - Sinon : récursion sur s[1:-1]

    Complexité : O(n)

    Note pédagogique :
    - Version élégante conceptuellement
    - Crée beaucoup de sous-chaînes (coût mémoire)
    - Version itérative (deux pointeurs) plus efficace en pratique

    Exemple : is_palindrome_recursive("radar")
        "radar" : r == r → is_palindrome_recursive("ada")
        "ada" : a == a → is_palindrome_recursive("d")
        "d" : longueur 1 → True
    """
    # Cas de base
    if len(s) <= 1:
        return True

    # Comparer premier et dernier caractère
    if s[0] != s[-1]:
        return False

    # Récursion sur la sous-chaîne sans les extrémités
    return is_palindrome_recursive(s[1:-1])


def factorial_recursive(n: int) -> int:
    """Calcule la factorielle de manière récursive.

    Approche : Récursion directe sur la définition n! = n × (n-1)!
    Cas de base : 0! = 1

    Complexité : O(n)

    Note pédagogique :
    - Exemple classique de récursion simple
    - Version récursive élégante et naturelle
    - Attention aux limites :
      * Python limite ~1000 appels récursifs
      * 1000! est un nombre gigantesque (dépasse capacité mémoire)

    Trace pour factorial_recursive(4) :
        factorial_recursive(4)
         = 4 × factorial_recursive(3)
         = 4 × 3 × factorial_recursive(2)
         = 4 × 3 × 2 × factorial_recursive(1)
         = 4 × 3 × 2 × 1 × factorial_recursive(0)
         = 4 × 3 × 2 × 1 × 1
         = 24
    """
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
