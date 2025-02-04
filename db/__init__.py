import sqlite3

def init_db():
    try:
        conn = sqlite3.connect("db/taches.db")
        cursor = conn.cursor()

        # Créer la table si elle n'existe pas encore
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS taches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            description TEXT,
            date_limite TEXT,
            priorite INTEGER DEFAULT 0
        )
        """)

        # Vérifier et ajouter les colonnes manquantes
        cursor.execute("PRAGMA table_info(taches)")
        columns = [col[1] for col in cursor.fetchall()]  # Liste des noms de colonnes

        required_columns = {
            "favori": "ALTER TABLE taches ADD COLUMN favori INTEGER DEFAULT 0"
        }

        for column, query in required_columns.items():
            if column not in columns:
                print(f"Ajout de la colonne '{column}' à la table 'taches'.")
                cursor.execute(query)

        conn.commit()
        print("Base de données initialisée avec succès.")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'initialisation de la base de données : {e}")
    finally:
        conn.close()
