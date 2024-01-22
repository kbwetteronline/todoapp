from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfiguration der Datenbank
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

# Initialisierung der SQLAlchemy-Erweiterung
db = SQLAlchemy(app)