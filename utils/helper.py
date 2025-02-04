from datetime import datetime

def convertir_date(date_chaine):
    """
    Convertit une chaîne de caractères en objet datetime.
    :param date_chaine: Date au format "YYYY-MM-DD".
    :return: Objet datetime ou None si la chaîne est invalide.
    """
    try:
        return datetime.strptime(date_chaine, "%Y-%m-%d")
    except ValueError:
        return None

def verifier_format_date(date_chaine):
    """
    Vérifie si une chaîne respecte le format "YYYY-MM-DD".
    :param date_chaine: Chaîne de caractères représentant une date.
    :return: True si le format est valide, False sinon.
    """
    return convertir_date(date_chaine) is not None
