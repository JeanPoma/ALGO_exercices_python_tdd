from __future__ import annotations


def tri_bulle(lst: list[int]) -> list[int]:
    """Tri à bulles (ne pas modifier `lst`).
    Pseudocode:
    1. Créer une copie de `lst` pour éviter la mutation.
    2. Répéter jusqu'à ce que la liste soit triée :
        - Parcourir la liste et comparer chaque paire d'éléments adjacents.
        - Si un élément est plus grand que le suivant, les échanger.
    3. Retourner la liste triée.
    """
    raise NotImplementedError


def tri_insertion(lst: list[int]) -> list[int]:
    """Tri par insertion (ne pas modifier `lst`).
    Pseudocode:
    1. Créer une copie de `lst` pour éviter la mutation.
    2. Pour chaque élément de la liste à partir de l'indice 1 :
        - Comparer cet élément avec les éléments précédents.
        - Déplacer les éléments plus grands vers la droite.
        - Insérer l'élément à la position correcte.
    3. Retourner la liste triée.
    """
    raise NotImplementedError


def tri_selection(lst: list[int]) -> list[int]:
    """Tri par sélection (ne pas modifier `lst`).
    Pseudocode:
    1. Créer une copie de `lst` pour éviter la mutation.
    2. Pour chaque position de la liste :
        - Trouver l'indice du plus petit élément du sous-tableau restant.
        - Échanger le plus petit élément avec l'élément à la position actuelle.
    3. Retourner la liste triée.
    """
    raise NotImplementedError


def tri_shell(lst: list[int]) -> list[int]:
    """Tri de Shell (ne pas modifier `lst`).
    Pseudocode:
    1. Créer une copie de `lst` pour éviter la mutation.
    2. Initialiser un intervalle basé sur la taille de la liste (par exemple, N//2).
    3. Diminuer progressivement l'intervalle jusqu'à 1 :
        - Pour chaque sous-liste formée par l'intervalle :
            - Appliquer un tri par insertion localement.
    4. Retourner la liste triée.
    """
    raise NotImplementedError


def tri_tas(lst: list[int]) -> list[int]:
    """Tri par tas (ne pas modifier `lst`).
    Pseudocode:
    1. Créer une copie de `lst` pour éviter la mutation.
    2. Construire un tas max à partir de la liste.
    3. Répéter jusqu'à ce que le tas soit réduit :
        - Échanger le premier (le maximum) avec le dernier élément du tas.
        - Réduire la taille du tas.
        - Appliquer la réorganisation du tas (heapify).
    4. Retourner la liste triée.
    """
    raise NotImplementedError


def tri_rapide(lst: list[int]) -> list[int]:
    """Quicksort récursif (ne pas modifier `lst`).
    Pseudocode:
    1. Si la liste a une longueur de 0 ou 1, elle est déjà triée.
    2. Choisir un pivot (typiquement le premier élément ou un aléatoire).
    3. Diviser la liste :
        - Une partie avec tous les éléments plus petits que le pivot.
        - Une partie avec tous les éléments plus grands ou égaux au pivot.
    4. Appliquer récursivement Quicksort sur les deux parties.
    5. Combiner les résultats de manière triée et inclure le pivot.
    6. Retourner la liste triée.
    """
    raise NotImplementedError
