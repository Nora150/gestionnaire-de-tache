Membres du groupe 
-AHOUILIHOUA yan MASSI1 
-KPEIDJA Midia MAGIRE1
-OGOUCHINA Nora MIAD1
Gestionnaire de Tâches – README
Description du Projet
Cette application est un gestionnaire de tâches qui permet aux utilisateurs d'ajouter, de modifier, de supprimer et de prioriser des tâches. L'objectif principal est de fournir une solution pratique pour organiser et suivre les activités quotidiennes. L'application inclut une interface utilisateur intuitive, un système de stockage fiable et des notifications pour rappeler les tâches importantes.
Fonctionnalités Principales
1.	Ajout de tâches : Les utilisateurs peuvent ajouter de nouvelles tâches avec des détails comme le titre, la description, la priorité et une date d'échéance.
2.	Modification de tâches : Possibilité de mettre à jour les détails d'une tâche existante.
3.	Suppression de tâches : Les utilisateurs peuvent supprimer les tâches terminées ou obsolètes.
4.	Priorisation des tâches : Classement des tâches en fonction de leur importance ou de leur urgence.
5.	Stockage des données : Toutes les tâches sont sauvegardées dans une base de données SQLite pour assurer leur persistance.
6.	Notifications : Des rappels automatiques informent les utilisateurs des tâches à venir.

Technologies Utilisées
•	Langage de programmation : Python 3.x
•	Interface utilisateur :Tkinter 
•	Base de données : SQLite
•	Bibliothèques Python :
o	sqlite3 : Gestion de la base de données
o	datetime : Gestion des dates et heures

Installation et Exécution
Prérequis
•	Python 3.x doit être installé sur votre système.
•	Les bibliothèques suivantes doivent être installées :
Instructions d'Installation
1.	Clonez ce dépôt sur votre machine locale :
git clone <URL_du_dépôt>
2.	Accédez au répertoire du projet :
cd gestionnaire-de-taches
3.	Lancez l'application :
python main.py


Guide d'Utilisation
1.	Démarrage de l'application : Lancer le fichier main.py pour ouvrir l'interface utilisateur.
2.	Ajout de tâches :
•	Cliquez sur le bouton "Ajouter une tâche".
•	Remplissez les champs requis 
•	Cliquez sur "Enregistrer".
3.	Modification de tâches :
•	Sélectionnez une tâche dans la liste.
•	Cliquez sur "Modifier" et effectuez les changements.
•	Cliquez sur "Mettre à jour".
4.	Suppression de tâches :
•	Sélectionnez une tâche et cliquez sur "Supprimer".
5.	Priorisation des tâches :
•	Les tâches sont affichées dans un ordre basé sur leur priorité et leur date d'échéance.
6.	Notifications :
•	Recevez des rappels pour les tâches urgentes (assurez-vous que les notifications sont activées sur votre système).
Améliorations Futures
•	Ajouter une fonctionnalité de synchronisation cloud pour accéder aux tâches sur plusieurs appareils.
•	Intégrer une recherche avancée pour filtrer les tâches.
•	Permettre la personnalisation des notifications.
