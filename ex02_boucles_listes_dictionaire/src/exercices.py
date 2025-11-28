from __future__ import annotations


# =============================================================================
# LISTES (Lists)
# =============================================================================


def somme_pairs(nums: list[int]) -> int:
    """Calcule la somme de tous les nombres pairs.

    Approche : Itération avec condition - accumulation des pairs uniquement.
    Complexité : O(n) où n = longueur de la liste

    Note pédagogique : Deux approches possibles :
    - Boucle for avec if (présentée ici)
    - Compréhension de liste : sum([n for n in nums if n % 2 == 0])
    """
    somme = 0
    for n in nums:
        if n % 2 == 0:
            somme += n
    return somme


def compter_occurrences(items: list[int], valeur: int) -> int:
    """Compte le nombre d'occurrences d'une valeur dans une liste.

    Approche : Compteur incrémenté à chaque correspondance.
    Complexité : O(n) - parcours complet de la liste

    Note pédagogique : Python fournit items.count(valeur) mais on implémente
    l'algorithme pour comprendre le mécanisme de comptage.
    """
    compteur = 0
    for item in items:
        if item == valeur:
            compteur += 1
    return compteur


def table_multiplication(n: int) -> list[int]:
    """Retourne la table de multiplication de n (jusqu'à 10 inclus).

    Approche : Construction d'une liste avec n*1, n*2, ..., n*10.
    Complexité : O(1) - toujours 10 éléments

    Note pédagogique : Excellent exercice pour comprendre range() et append().
    Alternative : [n * i for i in range(1, 11)] avec list comprehension.
    """
    table = []
    for i in range(1, 11):
        table.append(n * i)
    return table


def trouver_maximum(nums: list[int]) -> int:
    """Trouve et retourne la valeur maximale dans la liste.

    Approche : Algorithme classique de recherche du maximum.
    1. Initialiser max_val avec le premier élément
    2. Parcourir tous les éléments suivants
    3. Mettre à jour max_val si on trouve plus grand

    Complexité : O(n) - un seul parcours

    Note pédagogique :
    - On pourrait utiliser max(nums) mais on veut comprendre l'algorithme
    - Initialiser à nums[0] implique que la liste ne doit pas être vide
    - Alternative : initialiser à float('-inf') et parcourir toute la liste
    """
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val


def calculer_moyenne(nums: list[int]) -> float:
    """Calcule et retourne la moyenne des valeurs.

    Approche : Somme des éléments / nombre d'éléments.
    Complexité : O(n) - parcours pour la somme

    Note pédagogique :
    - Moyenne = somme / effectif
    - Retourne un float (même si tous les éléments sont int)
    - Cas spécial : liste vide retourne 0
    """
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)


def compter_negatifs(nums: list[int]) -> int:
    """Compte le nombre d'entiers négatifs dans la liste.

    Approche : Compteur avec condition n < 0.
    Complexité : O(n) - parcours complet

    Note pédagogique : Similaire à somme_pairs(), mais on compte au lieu de sommer.
    Alternative avec sum : sum(1 for n in nums if n < 0)
    """
    compteur = 0
    for n in nums:
        if n < 0:
            compteur += 1
    return compteur


# =============================================================================
# CHAÎNES DE CARACTÈRES (Strings)
# =============================================================================


def compter_mots(phrase: str) -> int:
    """Compte le nombre de mots dans une chaîne.

    Approche : Utilisation de .split() qui découpe selon les espaces.
    Complexité : O(n) où n = longueur de la chaîne

    Note pédagogique :
    - split() sans argument découpe sur n'importe quel whitespace (espace, tab, newline)
    - Gère automatiquement les espaces multiples
    - "Hello  world" -> ["Hello", "world"] (2 mots)
    """
    return len(phrase.split())


def trouver_plus_long(items: list[str]) -> str:
    """Trouve et retourne le mot le plus long.

    Approche : Recherche du maximum basée sur len().
    Complexité : O(n * m) où n = nombre de mots, m = longueur moyenne

    Note pédagogique : Similaire à trouver_maximum() mais on compare les longueurs.
    En cas d'égalité, on retourne le premier trouvé.
    """
    if len(items) == 0:
        return ""
    plus_long = items[0]
    for mot in items:
        if len(mot) > len(plus_long):
            plus_long = mot
    return plus_long


def convertir_majuscule(items: str) -> str:
    """Convertit une chaîne en majuscules.

    Approche : Utilisation de la méthode .upper().
    Complexité : O(n) où n = longueur de la chaîne

    Note pédagogique : Python fournit upper() et lower() pour les conversions.
    On pourrait aussi implémenter caractère par caractère avec ord()/chr().
    """
    return items.upper()


def compter_mots_commencant_par(items: str, lettre: str) -> int:
    """Compte les mots commençant par une lettre donnée.

    Approche :
    1. Découper la chaîne en mots avec split()
    2. Pour chaque mot, vérifier si le premier caractère correspond
    3. Utiliser lower() pour ignorer la casse

    Complexité : O(n) où n = nombre de mots

    Note pédagogique : Attention à gérer la casse (lettre.lower()).
    """
    compteur = 0
    for mot in items.split():
        if mot.lower().startswith(lettre.lower()):
            compteur += 1
    return compteur


def trouver_mot_finissant_par(items: str, suffixe: str) -> list[str]:
    """Trouve tous les mots qui se terminent par un suffixe donné.

    Approche :
    1. Découper en mots
    2. Filtrer ceux qui se terminent par le suffixe
    3. Utiliser .endswith() pour le test

    Complexité : O(n * m) où n = nombre de mots, m = longueur du suffixe

    Note pédagogique : Construction d'une nouvelle liste par filtrage.
    Alternative élégante : [mot for mot in items.split() if mot.endswith(suffixe)]
    """
    resultats = []
    for mot in items.split():
        if mot.endswith(suffixe):
            resultats.append(mot)
    return resultats


def compter_caracteres(s: str, char: str) -> int:
    """Compte le nombre d'occurrences d'un caractère.

    Approche : Compteur incrémenté à chaque correspondance.
    Complexité : O(n) où n = longueur de la chaîne

    Note pédagogique : Python fournit s.count(char), mais on implémente
    pour comprendre l'algorithme de comptage.
    """
    compteur = 0
    for c in s:
        if c == char:
            compteur += 1
    return compteur


def inverser_chaine(s: str) -> str:
    """Inverse et retourne la chaîne de caractères.

    Approche : Utilisation du slicing Python avec pas négatif.
    Complexité : O(n) - création d'une nouvelle chaîne

    Note pédagogique :
    - s[::-1] est l'idiome Python pour inverser une séquence
    - Alternative : ''.join(reversed(s))
    - Alternative manuelle : boucle for de la fin au début
    """
    return s[::-1]


def trouver_occurrences_chaine(s: str, c: str) -> int:
    """Compte les occurrences d'une sous-chaîne dans une chaîne.

    Approche : Utiliser la méthode .count() pour compter les occurrences.
    Complexité : O(n * m) où n = len(s), m = len(c)

    Note pédagogique : Différent de compter_caracteres() - ici on compte
    les occurrences d'une SOUS-CHAÎNE, pas d'un caractère unique.
    """
    return s.count(c)


# =============================================================================
# TUPLES (Tuples - immutables)
# =============================================================================


def somme_pairs_tuples(nums: tuple[int, ...]) -> int:
    """Calcule la somme de tous les nombres pairs dans un tuple.

    Approche : Identique à somme_pairs() mais sur un tuple.
    Complexité : O(n)

    Note pédagogique : Les tuples et listes se parcourent de la même façon.
    La seule différence : les tuples sont immutables (on ne peut pas les modifier).
    """
    somme = 0
    for n in nums:
        if n % 2 == 0:
            somme += n
    return somme


def compter_occurrences_tuples(items: tuple[int, ...], valeur: int) -> int:
    """Compte le nombre d'occurrences d'une valeur dans un tuple.

    Approche : Identique à compter_occurrences() mais sur un tuple.
    Complexité : O(n)

    Note pédagogique : Même logique que pour les listes.
    """
    compteur = 0
    for item in items:
        if item == valeur:
            compteur += 1
    return compteur


def table_multiplication_tuples(n: int) -> tuple[int, ...]:
    """Retourne la table de multiplication sous forme de tuple.

    Approche : Construire une liste puis convertir en tuple.
    Complexité : O(1) - toujours 10 éléments

    Note pédagogique : On construit d'abord une liste (mutable),
    puis on la convertit en tuple (immutable).
    Alternative : tuple(n * i for i in range(1, 11))
    """
    table = []
    for i in range(1, 11):
        table.append(n * i)
    return tuple(table)


def trouver_maximum_tuples(nums: tuple[int, ...]) -> int:
    """Trouve et retourne le nombre maximum d'un tuple.

    Approche : Identique à trouver_maximum() mais sur un tuple.
    Complexité : O(n)

    Note pédagogique : Même algorithme que pour les listes.
    """
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val


def calculer_moyenne_tuples(nums: tuple[int, ...]) -> float:
    """Calcule et retourne la moyenne des nombres dans un tuple.

    Approche : Somme / effectif.
    Complexité : O(n)

    Note pédagogique : Identique à calculer_moyenne().
    """
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)


# =============================================================================
# SETS (Ensembles - pas de doublons, pas d'ordre)
# =============================================================================


def somme_pairs_sets(nums: set[int]) -> int:
    """Calcule la somme de tous les nombres pairs dans un set.

    Approche : Identique aux listes/tuples mais sur un set.
    Complexité : O(n)

    Note pédagogique : Les sets éliminent automatiquement les doublons,
    donc chaque valeur n'est comptée qu'une fois.
    """
    somme = 0
    for n in nums:
        if n % 2 == 0:
            somme += n
    return somme


def compter_occurrences_sets(items: set[int], valeur: int) -> int:
    """Vérifie si une valeur existe dans le set (0 ou 1).

    Approche : Comme les sets n'ont pas de doublons, on retourne 0 ou 1.
    Complexité : O(1) - recherche dans un set est constante en moyenne

    Note pédagogique : C'est un cas particulier !
    - Si valeur dans le set -> retourne 1
    - Sinon -> retourne 0
    Les sets ne peuvent pas avoir de doublons par définition.
    """
    return 1 if valeur in items else 0


def table_multiplication_sets(n: int) -> set[int]:
    """Retourne la table de multiplication sous forme de set.

    Approche : Construction puis conversion en set.
    Complexité : O(1) - toujours 10 éléments

    Note pédagogique : Set garantit l'unicité (mais ici pas de doublons de toute façon).
    """
    table = set()
    for i in range(1, 11):
        table.add(n * i)
    return table


def trouver_maximum_sets(nums: set[int]) -> int:
    """Trouve et retourne le nombre maximum d'un set.

    Approche : Même algorithme que pour les listes.
    Complexité : O(n)

    Note pédagogique : On peut utiliser max(nums) directement,
    mais on implémente l'algorithme.
    """
    max_val = float('-inf')
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val


def compter_negatifs_sets(nums: set[int]) -> int:
    """Compte le nombre de nombres négatifs dans un set.

    Approche : Compteur avec condition n < 0.
    Complexité : O(n)

    Note pédagogique : Identique à compter_negatifs() pour les listes.
    """
    compteur = 0
    for n in nums:
        if n < 0:
            compteur += 1
    return compteur


# =============================================================================
# DICTIONNAIRES (Dictionaries - paires clé-valeur)
# =============================================================================


def ajouter_element(d: dict, cle: str, valeur: any) -> dict:
    """Ajoute une clé et sa valeur dans un dictionnaire (mutation in-place).

    Approche : Modification directe du dictionnaire.
    Complexité : O(1)

    Note pédagogique :
    - Cette fonction MODIFIE le dictionnaire passé en paramètre
    - dict[cle] = valeur ajoute ou remplace la valeur
    - Si la clé existe déjà, la valeur est remplacée
    """
    d[cle] = valeur
    return d


def supprimer_element(d: dict, cle: str) -> dict:
    """Supprime une clé et sa valeur d'un dictionnaire (mutation in-place).

    Approche : Suppression directe avec del.
    Complexité : O(1)

    Note pédagogique :
    - Cette fonction MODIFIE le dictionnaire passé en paramètre
    - On utilise del pour supprimer une entrée
    - Alternative : d.pop(cle) retourne la valeur supprimée
    """
    del d[cle]
    return d


def fusionner_dictionnaires(d1: dict, d2: dict) -> dict:
    """Fusionne deux dictionnaires (d2 écrase d1 en cas de conflit).

    Approche : Copie de d1 puis mise à jour avec d2.
    Complexité : O(n + m) où n, m = tailles des dicts

    Note pédagogique :
    - .update() ajoute/remplace les clés de d2 dans d1
    - Les valeurs de d2 ont la priorité en cas de conflit
    - Python 3.9+ permet : d1 | d2
    """
    resultat = d1.copy()
    resultat.update(d2)
    return resultat


def inverser_dictionnaire(d: dict) -> dict:
    """Inverse un dictionnaire, échangeant les clés et les valeurs.

    Approche : Construire un nouveau dict avec valeur -> clé.
    Complexité : O(n)

    Note pédagogique :
    - ATTENTION : Si plusieurs clés ont la même valeur, seule la dernière sera conservée
    - Exemple : {a: 1, b: 1} -> {1: b} (la clé 'a' est perdue)
    - Pour gérer les doublons : utiliser dict[valeur] = liste de clés
    """
    inverse = {}
    for cle, valeur in d.items():
        inverse[valeur] = cle
    return inverse


def compter_valeurs(d: dict) -> int:
    """Compte combien de paires clé-valeur sont dans le dictionnaire.

    Approche : Utilisation de len().
    Complexité : O(1)

    Note pédagogique : len(dict) retourne le nombre de clés.
    """
    return len(d)


def trouver_valeur_maximale(d: dict) -> any:
    """Trouve et retourne la valeur la plus grande dans un dictionnaire.

    Approche : Parcours des valeurs avec recherche du maximum.
    Complexité : O(n)

    Note pédagogique :
    - On utilise d.values() pour parcourir uniquement les valeurs
    - Alternative élégante : max(d.values())
    """
    valeurs = list(d.values())
    max_val = valeurs[0]
    for v in valeurs:
        if v > max_val:
            max_val = v
    return max_val


def trouver_cle_par_valeur(d: dict, valeur: any) -> str:
    """Retourne la première clé correspondant à une valeur donnée.

    Approche : Parcours des paires clé-valeur jusqu'à trouver la première correspondance.
    Complexité : O(n) pire cas

    Note pédagogique :
    - Retourne la PREMIÈRE clé trouvée avec cette valeur
    - Si plusieurs clés ont la même valeur, seule la première est retournée
    - Retourne None si aucune clé ne correspond (sera traité par le test)
    """
    for cle, val in d.items():
        if val == valeur:
            return cle
    return None


def verifier_cle_existe(d: dict, cle: str) -> bool:
    """Vérifie si une clé existe dans le dictionnaire.

    Approche : Utilisation de l'opérateur 'in'.
    Complexité : O(1) en moyenne (table de hachage)

    Note pédagogique :
    - 'cle in d' est l'idiome Python recommandé
    - Alternative : d.get(cle) is not None (mais None peut être une valeur valide)
    """
    return cle in d


def valeurs_uniques(d: dict) -> set:
    """Retourne toutes les valeurs uniques dans un dictionnaire sous forme de set.

    Approche : Conversion des valeurs en set (élimine les doublons).
    Complexité : O(n)

    Note pédagogique :
    - set() élimine automatiquement les doublons
    - Si toutes les valeurs sont différentes, len(set(d.values())) == len(d)
    """
    return set(d.values())


def mettre_a_jour_valeur(d: dict, cle: str, nouvelle_valeur: any) -> dict:
    """Met à jour une valeur associée à une clé ou en ajoute une nouvelle (mutation in-place).

    Approche : Assignation directe.
    Complexité : O(1)

    Note pédagogique :
    - Cette fonction MODIFIE le dictionnaire passé en paramètre
    - Si la clé existe : mise à jour de la valeur
    - Si la clé n'existe pas : ajout d'une nouvelle entrée
    - Même comportement que ajouter_element()
    """
    d[cle] = nouvelle_valeur
    return d
