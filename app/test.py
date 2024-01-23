import unittest
from flask import Flask
from flask_testing import TestCase
from routes import app, db, Task

class FlaskTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        with app.app_context():
            db.init_app(app)
            db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_task(self):
        test_task = Task(title="Test Delete Task", description="Test Delete Description", done=False)
        db.session.add(test_task)
        db.session.commit()
        response = self.client.post(f'/delete_task/{test_task.id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        test_task = Task.query.get(test_task.id)
        self.assertIsNone(test_task)

if __name__ == '__main__':
    unittest.main()