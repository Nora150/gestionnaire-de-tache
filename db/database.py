import sqlite3

# Initialiser la base de données
def init_db():
    conn = sqlite3.connect("db/taches.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS taches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT NOT NULL,
        description TEXT,
        date_limite TEXT,
        priorite INTEGER DEFAULT 0,
        favori INTEGER DEFAULT 0  -- 0 = pas favori, 1 = favori
    )
    """)
    conn.commit()
    conn.close()

# Ajouter une tâche
def ajouter_tache(titre, description, date_limite, priorite=0):
    conn = sqlite3.connect("db/taches.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO taches (titre, description, date_limite, priorite, favori)
    VALUES (?, ?, ?, ?, ?)
    """, (titre, description, date_limite, priorite, 0))  # Favori par défaut à 0
    conn.commit()
    conn.close()

# Lire toutes les tâches
def lire_taches():
    conn = sqlite3.connect("db/taches.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM taches ORDER BY favori DESC, priorite DESC")
    taches = cursor.fetchall()
    conn.close()
    return taches

# Supprimer une tâche
def supprimer_tache(tache_id):
    conn = sqlite3.connect("db/taches.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM taches WHERE id = ?", (tache_id,))
    conn.commit()
    conn.close()

# Modifier une tâche
def modifier_tache(tache_id, titre=None, description=None, date_limite=None, priorite=None):
    conn = sqlite3.connect("db/taches.db")
    cursor = conn.cursor()

    # Construire dynamiquement la requête SQL en fonction des champs modifiés
    champs = []
    valeurs = []

    if titre:
        champs.append("titre = ?")
        valeurs.append(titre)
    if description:
        champs.append("description = ?")
        valeurs.append(description)
    if date_limite:
        champs.append("date_limite = ?")
        valeurs.append(date_limite)
    if priorite is not None:
        champs.append("priorite = ?")
        valeurs.append(priorite)

    # Ajouter l'ID de la tâche à la liste des valeurs
    valeurs.append(tache_id)

    # Construire la requête SQL
    sql = f"UPDATE taches SET {', '.join(champs)} WHERE id = ?"
    cursor.execute(sql, valeurs)

    conn.commit()
    conn.close()

# Ajouter une tâche aux favoris
def ajouter_aux_favoris(tache_id):
    conn = sqlite3.connect("db/taches.db")
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE taches
    SET favori = 1
    WHERE id = ?
    """, (tache_id,))
    conn.commit()
    conn.close()
