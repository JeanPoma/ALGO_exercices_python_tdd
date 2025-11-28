from __future__ import annotations


def tri_bulle(lst: list[int]) -> list[int]:
    """Tri à bulles (Bubble Sort) - ne modifie pas lst.

    Principe : Comparer et échanger les éléments adjacents jusqu'à ce que
    la liste soit triée. Les plus grands éléments "remontent" vers la fin.

    Algorithme :
    1. Parcourir la liste plusieurs fois
    2. À chaque passage, comparer chaque paire d'éléments adjacents
    3. Si l'ordre est incorrect, les échanger
    4. Optimisation : après chaque passage, le dernier élément est en place

    Complexité :
    - Temps : O(n²) dans tous les cas (pire, moyen, meilleur*)
    - Espace : O(1) auxiliaire
    * Avec optimisation d'arrêt anticipé : O(n) si déjà trié

    Note pédagogique :
    - Algorithme le plus simple conceptuellement
    - Très inefficace en pratique (même pour petites listes)
    - Nom : les grands éléments "remontent" comme des bulles
    - Rarement utilisé en production (sauf cas très spéciaux)

    Exemple : [5, 2, 4, 1]
        Pass 1 : [2, 4, 1, 5] (5 remonte)
        Pass 2 : [2, 1, 4, 5] (4 remonte)
        Pass 3 : [1, 2, 4, 5] (2 remonte)
    """
    result = lst.copy()
    n = len(result)

    for i in range(n):
        # Optimisation : flag pour détecter si la liste est déjà triée
        echange = False
        # Chaque passage fait remonter le plus grand vers la fin
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                echange = True
        # Si aucun échange, la liste est triée
        if not echange:
            break

    return result


def tri_insertion(lst: list[int]) -> list[int]:
    """Tri par insertion (Insertion Sort) - ne modifie pas lst.

    Principe : Construire la liste triée élément par élément.
    Pour chaque élément, l'insérer à sa place dans la partie déjà triée.

    Algorithme :
    1. Considérer le premier élément comme trié
    2. Pour chaque élément suivant :
       - Le mémoriser temporairement
       - Décaler les éléments plus grands vers la droite
       - Insérer l'élément à la bonne position

    Complexité :
    - Temps : O(n²) pire cas, O(n) meilleur cas (déjà trié)
    - Espace : O(1) auxiliaire

    Note pédagogique :
    - Similaire à trier des cartes à jouer
    - Très efficace pour petites listes (< 50 éléments)
    - Excellent pour listes presque triées
    - Utilisé dans Timsort (tri Python) pour petits segments
    - Tri stable (préserve l'ordre des éléments égaux)

    Exemple : [5, 2, 4, 1]
        Étape 1 : [5] | [2, 4, 1]  →  [2, 5] | [4, 1]
        Étape 2 : [2, 5] | [4, 1]  →  [2, 4, 5] | [1]
        Étape 3 : [2, 4, 5] | [1]  →  [1, 2, 4, 5]
    """
    result = lst.copy()
    n = len(result)

    for i in range(1, n):
        # Élément à insérer
        key = result[i]
        j = i - 1

        # Décaler les éléments plus grands vers la droite
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1

        # Insérer l'élément à sa position
        result[j + 1] = key

    return result


def tri_selection(lst: list[int]) -> list[int]:
    """Tri par sélection (Selection Sort) - ne modifie pas lst.

    Principe : Sélectionner le plus petit élément et le placer au début,
    puis répéter pour le reste de la liste.

    Algorithme :
    1. Pour chaque position i :
       - Trouver le minimum dans result[i:]
       - Échanger result[i] avec ce minimum

    Complexité :
    - Temps : O(n²) dans tous les cas
    - Espace : O(1) auxiliaire

    Note pédagogique :
    - Nombre d'échanges minimal : O(n) (1 par position)
    - Comparaisons toujours O(n²) même si déjà trié
    - Utile quand l'écriture en mémoire est coûteuse
    - Tri non stable dans cette implémentation
    - Simple mais rarement utilisé en pratique

    Exemple : [5, 2, 4, 1]
        i=0 : Trouver min([5,2,4,1]) = 1  →  [1, 2, 4, 5]
        i=1 : Trouver min([2,4,5]) = 2    →  [1, 2, 4, 5]
        i=2 : Trouver min([4,5]) = 4      →  [1, 2, 4, 5]
        i=3 : Terminé
    """
    result = lst.copy()
    n = len(result)

    for i in range(n):
        # Trouver l'indice du minimum dans result[i:]
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j

        # Échanger avec la position actuelle
        result[i], result[min_idx] = result[min_idx], result[i]

    return result


def tri_shell(lst: list[int]) -> list[int]:
    """Tri de Shell (Shell Sort) - ne modifie pas lst.

    Principe : Généralisation du tri par insertion avec des "gaps".
    Trier d'abord des éléments éloignés, puis réduire l'écart.

    Algorithme :
    1. Commencer avec un grand gap (n // 2)
    2. Appliquer tri par insertion sur sous-listes espacées de gap
    3. Réduire le gap (gap // 2) et répéter
    4. Terminer avec gap = 1 (tri par insertion classique)

    Complexité :
    - Temps : O(n²) pire cas, O(n log n) à O(n^1.5) selon séquence de gaps
    - Espace : O(1) auxiliaire

    Note pédagogique :
    - Inventé par Donald Shell (1959)
    - Amélioration significative du tri par insertion
    - Performance dépend fortement de la séquence de gaps
    - Gaps classiques : n/2, n/4, n/8, ..., 1
    - Gaps optimaux : Knuth (3^k - 1)/2, Sedgewick, etc.
    - Excellent compromis simplicité/performance

    Exemple : [5, 2, 4, 1, 3] avec gaps [2, 1]
        Gap=2 : Trier [5,4,3] et [2,1] séparément  →  [3, 1, 4, 2, 5]
        Gap=1 : Tri insertion classique            →  [1, 2, 3, 4, 5]
    """
    result = lst.copy()
    n = len(result)
    gap = n // 2

    # Réduire progressivement le gap
    while gap > 0:
        # Tri par insertion avec gap
        for i in range(gap, n):
            key = result[i]
            j = i

            # Décaler les éléments espacés de gap
            while j >= gap and result[j - gap] > key:
                result[j] = result[j - gap]
                j -= gap

            result[j] = key

        gap //= 2

    return result


def tri_tas(lst: list[int]) -> list[int]:
    """Tri par tas (Heap Sort) - ne modifie pas lst.

    Principe : Construire un tas max, puis extraire le maximum répétitivement.

    Algorithme :
    1. Construire un tas max (heapify)
    2. Pour chaque position de la fin vers le début :
       - Échanger la racine (max) avec le dernier élément
       - Réduire la taille du tas
       - Réorganiser le tas (sift down)

    Complexité :
    - Temps : O(n log n) dans tous les cas
    - Espace : O(1) auxiliaire

    Note pédagogique :
    - Garantit O(n log n) même dans le pire cas (contrairement à quicksort)
    - Tri non stable
    - Utilise la structure de tas binaire (arbre complet)
    - Parent à l'indice i → enfants à 2i+1 et 2i+2
    - En pratique, souvent plus lent que quicksort (cache)
    - Base des files de priorité

    Structure de tas (exemple) :
            9
          /   \\
         7     6
        / \\   /
       5   4  3

    Représentation en array : [9, 7, 6, 5, 4, 3]
    """
    result = lst.copy()
    n = len(result)

    def heapify(arr: list[int], heap_size: int, root_idx: int) -> None:
        """Réorganise un sous-arbre pour maintenir la propriété de tas max."""
        largest = root_idx
        left = 2 * root_idx + 1
        right = 2 * root_idx + 2

        # Si l'enfant gauche existe et est plus grand que la racine
        if left < heap_size and arr[left] > arr[largest]:
            largest = left

        # Si l'enfant droit existe et est plus grand que le plus grand actuel
        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        # Si le plus grand n'est pas la racine, échanger et continuer
        if largest != root_idx:
            arr[root_idx], arr[largest] = arr[largest], arr[root_idx]
            heapify(arr, heap_size, largest)

    # Construire le tas max (heapify)
    # Commencer au dernier parent : (n // 2) - 1
    for i in range(n // 2 - 1, -1, -1):
        heapify(result, n, i)

    # Extraire les éléments un par un
    for i in range(n - 1, 0, -1):
        # Déplacer la racine (max) à la fin
        result[0], result[i] = result[i], result[0]
        # Réorganiser le tas réduit
        heapify(result, i, 0)

    return result


def tri_rapide(lst: list[int]) -> list[int]:
    """Tri rapide (Quicksort) récursif - ne modifie pas lst.

    Principe : Diviser pour régner avec un pivot.
    Partitionner autour d'un pivot, puis trier récursivement.

    Algorithme :
    1. Cas de base : liste de 0 ou 1 élément → déjà triée
    2. Choisir un pivot (ici : dernier élément)
    3. Partitionner :
       - Éléments < pivot à gauche
       - Éléments >= pivot à droite
    4. Trier récursivement les deux partitions
    5. Combiner : [gauche triée] + [pivot] + [droite triée]

    Complexité :
    - Temps : O(n log n) moyen, O(n²) pire cas (liste déjà triée)
    - Espace : O(log n) pile récursive

    Note pédagogique :
    - Un des algorithmes de tri les plus rapides en pratique
    - Utilisé dans de nombreuses bibliothèques standard
    - Performance dépend du choix du pivot :
      * Pivot aléatoire : évite le pire cas
      * Médiane de 3 : bon compromis
      * Dernier élément : simple mais pire cas sur liste triée
    - Tri non stable dans cette version
    - In-place version existe (plus complexe mais O(1) espace)

    Exemple : [5, 2, 4, 1, 3] avec pivot = 3
        Partition : [2, 1] + [3] + [5, 4]
        Récursion : tri_rapide([2,1]) et tri_rapide([5,4])
        Résultat : [1, 2, 3, 4, 5]
    """
    # Cas de base
    if len(lst) <= 1:
        return lst.copy()

    # Choisir le pivot (ici : dernier élément)
    pivot = lst[-1]

    # Partitionner
    gauche = [x for x in lst[:-1] if x < pivot]
    droite = [x for x in lst[:-1] if x >= pivot]

    # Trier récursivement et combiner
    return tri_rapide(gauche) + [pivot] + tri_rapide(droite)
