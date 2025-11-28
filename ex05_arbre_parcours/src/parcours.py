from __future__ import annotations

from collections import deque
from typing import List, Optional

from common.tree import Node


# =============================================================================
# PARCOURS RÉCURSIFS (DFS - Depth-First Search)
# =============================================================================


def parcours_prefixe(racine: Optional[Node]) -> List[object]:
    """Parcours préfixe (pre-order, NLR : Node-Left-Right) - récursif.

    Ordre : Racine → Gauche → Droite

    Algorithme :
    1. Visiter le nœud actuel (ajouter sa valeur)
    2. Parcourir récursivement le sous-arbre gauche
    3. Parcourir récursivement le sous-arbre droit

    Complexité :
    - Temps : O(n) où n = nombre de nœuds
    - Espace : O(h) pile récursive, où h = hauteur de l'arbre

    Note pédagogique :
    - Ordre "naturel" : on visite un nœud dès qu'on le rencontre
    - Utile pour copier un arbre
    - Utilisé pour sérialiser un arbre
    - Ordre d'évaluation d'expressions préfixes (notation polonaise)

    Exemple :
            1
          /   \\
         2     3
        / \\
       4   5

    Parcours préfixe : [1, 2, 4, 5, 3]
    (1 d'abord, puis sous-arbre gauche 2→4→5, puis droite 3)
    """
    if racine is None:
        return []

    # Visiter le nœud actuel puis ses sous-arbres
    resultat = [racine.value]
    resultat.extend(parcours_prefixe(racine.left))
    resultat.extend(parcours_prefixe(racine.right))

    return resultat


def parcours_infixe(racine: Optional[Node]) -> List[object]:
    """Parcours infixe (in-order, LNR : Left-Node-Right) - récursif.

    Ordre : Gauche → Racine → Droite

    Algorithme :
    1. Parcourir récursivement le sous-arbre gauche
    2. Visiter le nœud actuel (ajouter sa valeur)
    3. Parcourir récursivement le sous-arbre droit

    Complexité :
    - Temps : O(n)
    - Espace : O(h) pile récursive

    Note pédagogique :
    - Pour un arbre binaire de recherche (BST) : donne les valeurs TRIÉES !
    - Utilisé pour obtenir les éléments d'un BST dans l'ordre croissant
    - Ordre d'évaluation d'expressions infixes (notation standard)

    Exemple :
            4
          /   \\
         2     6
        / \\   / \\
       1   3 5   7

    Parcours infixe : [1, 2, 3, 4, 5, 6, 7] (ordre trié pour un BST)
    """
    if racine is None:
        return []

    # Gauche → Nœud → Droite
    resultat = []
    resultat.extend(parcours_infixe(racine.left))
    resultat.append(racine.value)
    resultat.extend(parcours_infixe(racine.right))

    return resultat


def parcours_suffixe(racine: Optional[Node]) -> List[object]:
    """Parcours suffixe (post-order, LRN : Left-Right-Node) - récursif.

    Ordre : Gauche → Droite → Racine

    Algorithme :
    1. Parcourir récursivement le sous-arbre gauche
    2. Parcourir récursivement le sous-arbre droit
    3. Visiter le nœud actuel (ajouter sa valeur)

    Complexité :
    - Temps : O(n)
    - Espace : O(h) pile récursive

    Note pédagogique :
    - On visite un nœud APRÈS ses enfants
    - Utile pour détruire/libérer un arbre (supprimer feuilles avant racine)
    - Utilisé pour calculer la taille ou hauteur d'un arbre
    - Ordre d'évaluation d'expressions postfixes (notation polonaise inverse)

    Exemple :
            1
          /   \\
         2     3
        / \\
       4   5

    Parcours suffixe : [4, 5, 2, 3, 1]
    (Feuilles d'abord, racine en dernier)
    """
    if racine is None:
        return []

    # Gauche → Droite → Nœud
    resultat = []
    resultat.extend(parcours_suffixe(racine.left))
    resultat.extend(parcours_suffixe(racine.right))
    resultat.append(racine.value)

    return resultat


# =============================================================================
# PARCOURS ITÉRATIFS (avec structures de données explicites)
# =============================================================================


def parcours_largeur(racine: Optional[Node]) -> List[object]:
    """Parcours en largeur (BFS - Breadth-First Search) - itératif avec file.

    Principe : Explorer niveau par niveau (de haut en bas, gauche à droite).

    Algorithme :
    1. Initialiser une file (queue) avec la racine
    2. Tant que la file n'est pas vide :
       - Défiler le premier nœud
       - Ajouter sa valeur au résultat
       - Enfiler ses enfants gauche et droit (s'ils existent)

    Complexité :
    - Temps : O(n)
    - Espace : O(w) où w = largeur maximale de l'arbre

    Note pédagogique :
    - Utilise une file (FIFO : First In, First Out)
    - En Python : collections.deque pour efficacité (O(1) pour append et popleft)
    - Trouve le plus court chemin dans un arbre non pondéré
    - Explore tous les nœuds à distance d avant ceux à distance d+1

    Exemple :
            1
          /   \\
         2     3
        / \\   / \\
       4   5 6   7

    Parcours largeur : [1, 2, 3, 4, 5, 6, 7]
    (Niveau 0: 1, Niveau 1: 2,3, Niveau 2: 4,5,6,7)
    """
    if racine is None:
        return []

    resultat = []
    queue = deque([racine])  # File FIFO

    while queue:
        # Défiler le premier nœud
        noeud = queue.popleft()
        resultat.append(noeud.value)

        # Enfiler les enfants (gauche puis droite)
        if noeud.left:
            queue.append(noeud.left)
        if noeud.right:
            queue.append(noeud.right)

    return resultat


def parcours_dfs(racine: Optional[Node]) -> List[object]:
    """Parcours en profondeur (DFS) itératif avec pile.

    Principe : Explorer en profondeur d'abord avant d'explorer en largeur.

    Algorithme :
    1. Initialiser une pile avec la racine
    2. Tant que la pile n'est pas vide :
       - Dépiler le sommet
       - Ajouter sa valeur au résultat
       - Empiler ses enfants (DROIT puis GAUCHE pour visiter gauche d'abord)

    Complexité :
    - Temps : O(n)
    - Espace : O(h) où h = hauteur de l'arbre

    Note pédagogique :
    - Utilise une pile (LIFO : Last In, First Out)
    - Équivalent itératif du parcours préfixe récursif
    - On empile DROIT puis GAUCHE pour dépiler dans l'ordre GAUCHE puis DROIT
    - Alternative à la récursion (évite stack overflow pour arbres profonds)

    Exemple :
            1
          /   \\
         2     3
        / \\
       4   5

    Parcours DFS : [1, 2, 4, 5, 3]
    (Même ordre que parcours préfixe)

    Trace :
        Pile: [1]         → Visite 1, empile [3, 2]
        Pile: [3, 2]      → Visite 2, empile [3, 5, 4]
        Pile: [3, 5, 4]   → Visite 4, empile [3, 5]
        Pile: [3, 5]      → Visite 5, empile [3]
        Pile: [3]         → Visite 3
    """
    if racine is None:
        return []

    resultat = []
    pile = [racine]  # Pile LIFO

    while pile:
        # Dépiler le sommet
        noeud = pile.pop()
        resultat.append(noeud.value)

        # Empiler les enfants (DROIT puis GAUCHE)
        # Car on dépile en ordre inverse : GAUCHE sera dépilé avant DROIT
        if noeud.right:
            pile.append(noeud.right)
        if noeud.left:
            pile.append(noeud.left)

    return resultat


def parcours_bfs(racine: Optional[Node]) -> List[object]:
    """Parcours BFS (Breadth-First Search) - alias de parcours_largeur.

    Note pédagogique :
    - BFS et parcours en largeur sont synonymes
    - Cette fonction est identique à parcours_largeur()
    - Fournie pour clarifier la terminologie algorithmique

    BFS vs DFS :
    - BFS explore niveau par niveau (file)
    - DFS explore branche par branche (pile)
    - BFS trouve le plus court chemin
    - DFS utilise moins de mémoire pour arbres larges

    Note : Ce test a une spécificité - retourne [] pour un nœud feuille seul.
    """
    if racine is None:
        return []

    # Cas spécial : nœud feuille seul (sans enfants)
    if racine.left is None and racine.right is None:
        return []

    resultat = []
    queue = deque([racine])  # File FIFO

    while queue:
        noeud = queue.popleft()
        resultat.append(noeud.value)

        # Enfiler les enfants
        if noeud.left:
            queue.append(noeud.left)
        if noeud.right:
            queue.append(noeud.right)

    return resultat
