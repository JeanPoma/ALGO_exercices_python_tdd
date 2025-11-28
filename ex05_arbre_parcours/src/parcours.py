from __future__ import annotations

from typing import List, Optional

from common.tree import Node


def parcours_prefixe(racine: Optional[Node]) -> List[object]:
    """
    Parcours préfixe (ou parcours en profondeur d'abord, version préfixe) :
    - Si le nœud racine est None, retourne une liste vide.
    - Ajoute la valeur du nœud racine à la liste de résultat.
    - Parcourt récursivement le sous-arbre gauche en utilisant la même méthode.
    - Parcourt récursivement le sous-arbre droit en utilisant la même méthode.
    - Combine les résultats et retourne la liste complète.
    """
    raise NotImplementedError


def parcours_infixe(racine: Optional[Node]) -> List[object]:
    """
    Parcours infixe :
    - Si le nœud racine est None, retourne une liste vide.
    - Parcourt récursivement le sous-arbre gauche en utilisant la même méthode.
    - Ajoute la valeur du nœud racine à la liste de résultat.
    - Parcourt récursivement le sous-arbre droit en utilisant la même méthode.
    - Combine les résultats et retourne la liste complète.
    """
    raise NotImplementedError


def parcours_suffixe(racine: Optional[Node]) -> List[object]:
    """
    Parcours suffixe (parcours post-ordre) :
    - Si le nœud racine est None, retourne une liste vide.
    - Parcourt récursivement le sous-arbre gauche en utilisant la même méthode.
    - Parcourt récursivement le sous-arbre droit en utilisant la même méthode.
    - Ajoute la valeur du nœud racine à la liste de résultat.
    - Combine les résultats et retourne la liste complète.
    """
    raise NotImplementedError


def parcours_largeur(racine: Optional[Node]) -> List[object]:
    """
    Parcours en largeur (utilisation d'une file) :
    - Si le nœud racine est None, retourne une liste vide.
    - Initialise une queue (file) contenant le nœud racine.
    - Pendant que la queue n'est pas vide :
        - Extraire le premier élément de la queue.
        - Ajouter la valeur de ce nœud à la liste de résultat.
        - Ajouter les sous-arbres gauche et droit à la fin de la queue s'ils ne sont pas None.
    - Retourne la liste de résultat.
    """
    raise NotImplementedError


def parcours_dfs(racine: Optional[Node]) -> List[object]:
    """
    Parcours en profondeur (Depth-First Search, basé sur une pile) :
    - Si le nœud racine est None, retourne une liste vide.
    - Initialise une pile contenant uniquement le nœud racine.
    - Pendant que la pile n'est pas vide :
        - Extraire le nœud en haut de la pile.
        - Ajouter la valeur de ce nœud à la liste de résultat.
        - Ajouter les sous-arbres droit et gauche (dans cet ordre) à la pile si présents.
    - Retourne la liste de résultat.
    """
    raise NotImplementedError


def parcours_bfs(racine: Optional[Node]) -> List[object]:
    """
    Parcours en largeur (Breadth-First Search, basé sur une file) :
    - Si le nœud racine est None, retourne une liste vide.
    - Initialise une file contenant uniquement le nœud racine.
    - Pendant que la file n'est pas vide :
        - Extraire le nœud en tête de la file.
        - Ajouter la valeur de ce nœud à la liste de résultat.
        - Ajouter les sous-arbres gauche et droit (dans cet ordre) à la file s'ils ne sont pas None.
    - Retourne la liste de résultat.
    """
    raise NotImplementedError

