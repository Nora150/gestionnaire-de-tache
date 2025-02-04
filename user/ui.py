import tkinter as tk
from tkinter import messagebox
from db.database import ajouter_tache, lire_taches, supprimer_tache, modifier_tache, ajouter_aux_favoris


class TaskManagerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestionnaire de Tâches")
        self.root.geometry("900x600")  # Taille ajustée pour inclure les nouvelles fonctionnalités

        self.titre_var = tk.StringVar()
        self.description_var = tk.StringVar()
        self.date_limite_var = tk.StringVar()
        self.priorite_var = tk.IntVar()

        self.create_widgets()
        self.update_task_list()

    def create_widgets(self):
        # Section supérieure (formulaire d'ajout ou modification)
        form_frame = tk.Frame(self.root, pady=10)
        form_frame.pack(fill=tk.X)

        tk.Label(form_frame, text="Titre :", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Entry(form_frame, textvariable=self.titre_var, width=30).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Description :", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Entry(form_frame, textvariable=self.description_var, width=30).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Date Limite (YYYY-MM-DD) :", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Entry(form_frame, textvariable=self.date_limite_var, width=30).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Priorité (0 - Faible, 1 - Haute) :", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Entry(form_frame, textvariable=self.priorite_var, width=30).grid(row=3, column=1, padx=5, pady=5)

        # Boutons d'ajout ou modification
        tk.Button(form_frame, text="Ajouter Tâche", command=self.ajouter_tache, bg="green", fg="white", font=("Arial", 10)).grid(row=4, column=0, pady=10)
        tk.Button(form_frame, text="Modifier Tâche", command=self.modifier_tache, bg="orange", fg="white", font=("Arial", 10)).grid(row=4, column=1, pady=10)

        # Section liste des tâches
        list_frame = tk.Frame(self.root)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.task_list = tk.Listbox(list_frame, font=("Arial", 12), width=70, height=15)
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        scrollbar = tk.Scrollbar(list_frame, command=self.task_list.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_list.config(yscrollcommand=scrollbar.set)

        # Section des boutons d'actions
        action_frame = tk.Frame(self.root, pady=10)
        action_frame.pack(fill=tk.X)

        tk.Button(action_frame, text="Lire Tâches", command=self.update_task_list, bg="blue", fg="white", font=("Arial", 10)).grid(row=0, column=0, padx=10)
        tk.Button(action_frame, text="Supprimer Tâche", command=self.supprimer_tache, bg="red", fg="white", font=("Arial", 10)).grid(row=0, column=1, padx=10)
        tk.Button(action_frame, text="Ajouter aux Favoris", command=self.ajouter_aux_favoris, bg="purple", fg="white", font=("Arial", 10)).grid(row=0, column=2, padx=10)

    def ajouter_tache(self):
        titre = self.titre_var.get()
        description = self.description_var.get()
        date_limite = self.date_limite_var.get()
        priorite = self.priorite_var.get()

        if not titre.strip():
            messagebox.showerror("Erreur", "Le titre est obligatoire.")
            return

        ajouter_tache(titre, description, date_limite, priorite)
        messagebox.showinfo("Succès", "Tâche ajoutée avec succès.")
        self.update_task_list()

    def supprimer_tache(self):
        selected_task = self.task_list.curselection()
        if not selected_task:
            messagebox.showerror("Erreur", "Veuillez sélectionner une tâche.")
            return

        task_id = self.task_list.get(selected_task).split(" - ")[0]
        supprimer_tache(task_id)
        messagebox.showinfo("Succès", "Tâche supprimée avec succès.")
        self.update_task_list()

    def modifier_tache(self):
        selected_task = self.task_list.curselection()
        if not selected_task:
            messagebox.showerror("Erreur", "Veuillez sélectionner une tâche à modifier.")
            return

        task_id = self.task_list.get(selected_task).split(" - ")[0]
        titre = self.titre_var.get()
        description = self.description_var.get()
        date_limite = self.date_limite_var.get()
        priorite = self.priorite_var.get()

        if not titre.strip():
            messagebox.showerror("Erreur", "Le titre est obligatoire.")
            return

        modifier_tache(task_id, titre=titre, description=description, date_limite=date_limite, priorite=priorite)
        messagebox.showinfo("Succès", "Tâche modifiée avec succès.")
        self.update_task_list()

    def ajouter_aux_favoris(self):
        selected_task = self.task_list.curselection()
        if not selected_task:
            messagebox.showerror("Erreur", "Veuillez sélectionner une tâche à ajouter aux favoris.")
            return

        task_id = self.task_list.get(selected_task).split(" - ")[0]
        ajouter_aux_favoris(task_id)
        messagebox.showinfo("Succès", "Tâche ajoutée aux favoris avec succès.")
        self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for tache in lire_taches():
            favori = "❤️" if tache[5] == 1 else ""  # Ajouter un cœur pour les favoris
            self.task_list.insert(tk.END, f"{tache[0]} - {tache[1]} ({tache[3]}) {favori}")

    def run(self):
        self.root.mainloop()


# Lancer l'application
if __name__ == "__main__":
    app = TaskManagerApp()
    app.run()
