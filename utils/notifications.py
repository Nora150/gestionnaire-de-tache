from datetime import datetime, timedelta
from db.database import lire_taches

def verifier_notifications():
    """
    Renvoie une liste des tâches à rappeler dont la date limite est proche (dans 3 jours).
    """
    taches = lire_taches()
    notifications = []
    today = datetime.now()
    for tache in taches:
        if tache[3]:
            date_limite = datetime.strptime(tache[3], "%Y-%m-%d")
            if today <= date_limite <= today + timedelta(days=3):
                notifications.append(f"Tâche '{tache[1]}' à terminer pour le {tache[3]}.")
    return notifications
