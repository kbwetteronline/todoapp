from flask import render_template, jsonify, request
from flask import Flask
from models import db, Task

# Flask-App erstellen
app = Flask(__name__)

# Funktion, um die App zu configurieren
def config_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        db.init_app(app)  # Datenbank initialisieren
        db.create_all()  # Alle Tabellen erstellen
    return app

# Route für die Startseite
@app.route('/')
def index():
    return render_template('index.html', tasks=Task.query.all()) # Vorlage rendern

# Route, um eine neue Aufgabe zu erstellen
@app.route('/create_task', methods=['POST'])
def create_task():
    title = request.form["title"]  # Titel der Aufgabe abrufen
    description = request.form.get("description", "")  # Beschreibung der Aufgabe abrufen
    new_task = Task(title=title, description=description , done=False)  # Neue Aufgabe erstellen
    db.session.add(new_task)  # Neue Aufgabe zur Datenbank hinzufügen
    db.session.commit()  # Änderungen speichern
    return render_template('index.html', tasks=Task.query.all())  # Webseite rendern

# Route, um eine Aufgabe als erledigt zu markieren
@app.route('/mark_done/<int:task_id>', methods=['POST'])
def mark_done(task_id):
    task = Task.query.get_or_404(task_id)  # Aufgabe abrufen
    task.done = True  # Als erledigt markieren
    db.session.commit()  # Änderungen speichern
    return render_template('index.html', tasks=Task.query.all())  # Webseite rendern

# Route, um eine Aufgabe zu löschen
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)  # Aufgabe abrufen
    db.session.delete(task)  # Aufgabe löschen
    db.session.commit()  # Änderungen speichern
    return render_template('index.html', tasks=Task.query.all())  # Webseite rendern

# App ausführen
if __name__ == '__main__':
    app = config_app()
    app.run(debug=True, port=8020, use_reloader=False)  # App ausführen