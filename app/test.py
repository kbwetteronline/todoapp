import unittest
from flask_testing import TestCase
from routes import app, db, Task

# Erstellen einer Testklasse, die von TestCase erbt
class FlaskTest(TestCase):

    # Funktion, um die App zu konfigurieren
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    # Methode, die vor jedem Test ausgeführt wird
    def setUp(self):
        with app.app_context():
            db.init_app(app)
            db.create_all()

    # Methode, die nach jedem Test ausgeführt wird
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Testmethode zum Testen der delete_task Route
    def test_delete_task(self):
        # Erstellen einer Test Task
        test_task = Task(title="Test Delete Task", description="Test Delete Description", done=False)
        db.session.add(test_task)
        db.session.commit()
        # Test Task mit der Route aus der Datenbank löschen
        response = self.client.post(f'/delete_task/{test_task.id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200) 
        test_task = Task.query.get(test_task.id) # Versuch Test Task aus der Datenbank abzurufen
        self.assertIsNone(test_task) # Test Task sollte nicht mehr in der Datenbank sein

if __name__ == '__main__':
    unittest.main() # Tests ausführen