from __future__ import annotations


def somme(a: int, b: int) -> int:
    """Retourne la somme de deux entiers.

    Approche : Addition simple - opération arithmétique de base.
    Complexité : O(1) - opération constante

    Note pédagogique : C'est la fonction la plus simple, elle introduit
    la syntaxe des fonctions Python avec type hints.
    """
    return a + b


def produit(a: int, b: int) -> int:
    """Retourne le produit de deux entiers.

    Approche : Multiplication simple - opération arithmétique de base.
    Complexité : O(1) - opération constante

    Note pédagogique : Similaire à somme(), mais avec l'opérateur *.
    """
    return a * b


def est_pair(n: int) -> bool:
    """Vrai si le nombre est pair.

    Approche : Utilisation de l'opérateur modulo (%) pour tester la divisibilité par 2.
    Un nombre est pair si le reste de sa division par 2 est 0.

    Complexité : O(1) - opération constante

    Note pédagogique : C'est un exemple classique d'utilisation du modulo.
    On pourrait aussi faire n & 1 == 0 (opération bit à bit), mais c'est moins lisible.
    """
    return n % 2 == 0


def est_voyelle(lettre: str) -> bool:
    """Vrai si la lettre est une voyelle.

    Approche : On vérifie si la lettre (en minuscule) appartient à l'ensemble des voyelles.
    On utilise .lower() pour gérer les majuscules et minuscules.

    Complexité : O(1) - la recherche dans un petit set est constante

    Note pédagogique : On pourrait aussi faire lettre.lower() in 'aeiouy' (string),
    mais un set est légèrement plus idiomatique Python pour un test d'appartenance.
    La conversion en minuscule évite de doubler la logique pour A-Z.
    """
    return lettre.lower() in {'a', 'e', 'i', 'o', 'u', 'y'}


def calcul_reduction(prix: float, taux: float) -> float:
    """Retourne le prix après remise (taux en pourcentage).

    Approche : Calcul du nouveau prix = prix - (prix * taux / 100)
    On peut aussi écrire : prix * (1 - taux / 100)

    Complexité : O(1) - opération arithmétique simple

    Note pédagogique : Attention aux validations !
    - Le taux doit être entre 0 et 100
    - Le prix devrait être positif
    - On lève une ValueError si le prix est négatif

    Exemple :
        calcul_reduction(100, 20) -> 80.0  (20% de réduction sur 100€)
    """
    if prix < 0:
        raise ValueError("Le prix ne peut pas être négatif")
    nouveau_prix = prix * (1 - taux / 100)
    # Ne pas retourner de prix négatif
    return max(0.0, nouveau_prix)


def est_bissextile(annee: int) -> bool:
    """Vrai si année bissextile (Grégorien).

    Règle complète :
    1. Une année est bissextile si elle est divisible par 4
    2. SAUF si elle est divisible par 100 (alors elle n'est PAS bissextile)
    3. SAUF si elle est divisible par 400 (alors elle EST bissextile)

    Approche : Tester les conditions de la plus spécifique à la plus générale.
    L'ordre des tests est crucial !

    Complexité : O(1) - 3 tests maximum

    Note pédagogique : C'est un excellent exercice de logique conditionnelle.
    Erreur fréquente : tester les conditions dans le mauvais ordre.

    Exemples :
        2000 : divisible par 400 -> bissextile ✓
        1900 : divisible par 100 mais pas 400 -> PAS bissextile ✗
        2004 : divisible par 4 mais pas 100 -> bissextile ✓
        2001 : non divisible par 4 -> PAS bissextile ✗
    """
    if annee % 400 == 0:
        return True
    if annee % 100 == 0:
        return False
    if annee % 4 == 0:
        return True
    return False


def racine_carree(x: float) -> float:
    """Retourne la racine carrée d'un nombre.

    Approche : Utilisation de l'opérateur puissance ** avec exposant 0.5
    Équivalent à math.sqrt(x) mais sans import externe.

    Complexité : O(1) - opération constante

    Note pédagogique : x ** 0.5 est équivalent à √x car x^(1/2) = √x
    Alternative : on pourrait implémenter la méthode de Newton-Raphson,
    mais ce serait over-engineering pour cet exercice.

    Validation : On lève une exception si x < 0
    (on ne peut pas calculer la racine carrée d'un nombre négatif dans ℝ).
    """
    if x < 0:
        raise ValueError("Impossible de calculer la racine carrée d'un nombre négatif")
    return x ** 0.5


def maximum_trois(a: int, b: int, c: int) -> int:
    """Renvoie le maximum de trois valeurs sans utiliser max().

    Approche : Comparaisons successives avec if/elif/else.
    On compare d'abord a et b, puis le résultat avec c.

    Complexité : O(1) - nombre constant de comparaisons

    Note pédagogique : Plusieurs approches possibles :
    - Imbrication de if: if a > b: return a if a > c else c ...
    - Ternaire : return a if a >= b and a >= c else (b if b >= c else c)
    - Simplification : max(a, max(b, c)) mais utilise max() donc interdit

    La solution présentée est la plus lisible pour des débutants.
    """
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c


def factorielle(n: int) -> int:
    """Retourne la factorielle d'un entier.

    Approche : Itération de 1 à n en accumulant le produit.
    n! = 1 × 2 × 3 × ... × n

    Cas particulier : 0! = 1 (par convention mathématique)

    Complexité : O(n) - on itère n fois

    Note pédagogique :
    1. Validation importante : on lève une ValueError pour n < 0
       car la factorielle n'est pas définie pour les nombres négatifs.
    2. Initialisation à 1 est cruciale (élément neutre de la multiplication).
    3. range(1, n+1) car range exclut la borne supérieure.

    Alternatives :
    - Récursive : plus élégante mais risque de stack overflow pour grand n
    - math.factorial(n) : mais on veut implémenter l'algorithme

    Exemples :
        factorielle(0) -> 1
        factorielle(5) -> 120  (1*2*3*4*5)
        factorielle(-1) -> ValueError
    """
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs")

    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat


def convertir_en_binaire(n: int) -> str:
    """Convertit un entier en représentation binaire.

    Approche : Algorithme de divisions successives par 2.
    On récupère les restes de droite à gauche, puis on inverse.

    Complexité : O(log n) - nombre de bits dans la représentation

    Note pédagogique :
    - On pourrait utiliser bin(n) qui retourne '0b101' et faire [2:] pour enlever '0b'
    - Mais ici on implémente l'algorithme classique pour comprendre le fonctionnement

    Algorithme :
    1. Cas particulier : 0 -> '0'
    2. Tant que n > 0 :
       - Ajouter (n % 2) à la représentation binaire
       - Diviser n par 2 (division entière)
    3. Inverser la chaîne car on a construit de droite à gauche

    Exemples :
        5 -> 101  (5 = 1*4 + 0*2 + 1*1)
        10 -> 1010  (10 = 1*8 + 0*4 + 1*2 + 0*1)

    Trace d'exécution pour n=5 :
        5 % 2 = 1, n = 5 // 2 = 2  -> '1'
        2 % 2 = 0, n = 2 // 2 = 1  -> '01'
        1 % 2 = 1, n = 1 // 2 = 0  -> '101'
        Inversion : '101'
    """
    if n == 0:
        return '0'

    binaire = ''
    while n > 0:
        binaire = str(n % 2) + binaire  # On ajoute au début pour construire de gauche à droite
        n = n // 2  # Division entière

    return binaire
