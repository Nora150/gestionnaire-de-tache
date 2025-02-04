from db.database import init_db
from user.ui import TaskManagerApp

# Initialiser la base de données
init_db()

# Lancer l'application Tkinter
if __name__ == "__main__":
    app = TaskManagerApp()
    app.run()
