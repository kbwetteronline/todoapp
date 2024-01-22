from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy-Instanz erstellen
db = SQLAlchemy()

# Task-Modell definieren
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primärschlüssel
    title = db.Column(db.String(50), nullable=False)  # Titel der Aufgabe, darf nicht null sein
    description = db.Column(db.String(100))  # Beschreibung der Aufgabe, darf null sein
    done = db.Column(db.Boolean, default=False)  # Status der Aufgabe, standardmäßig False
