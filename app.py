# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from db.database import init_db, ajouter_tache, lire_taches, supprimer_tache, modifier_tache, ajouter_aux_favoris

app = Flask(__name__)

# Initialiser la base de données
init_db()

@app.route("/")
def index():
    taches = lire_taches()
    return render_template("index.html", taches=taches)

@app.route("/ajouter", methods=["POST"])
def ajouter():
    titre = request.form.get("titre")
    description = request.form.get("description")
    date_limite = request.form.get("date_limite")
    priorite = request.form.get("priorite", 0)
    ajouter_tache(titre, description, date_limite, int(priorite))
    return redirect(url_for("index"))

@app.route("/supprimer/<int:tache_id>")
def supprimer(tache_id):
    supprimer_tache(tache_id)
    return redirect(url_for("index"))

@app.route("/modifier/<int:tache_id>", methods=["POST"])
def modifier(tache_id):
    titre = request.form.get("titre")
    description = request.form.get("description")
    date_limite = request.form.get("date_limite")
    priorite = request.form.get("priorite", 0)
    modifier_tache(tache_id, titre=titre, description=description, date_limite=date_limite, priorite=int(priorite))
    return redirect(url_for("index"))

@app.route("/favori/<int:tache_id>")
def favori(tache_id):
    ajouter_aux_favoris(tache_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
