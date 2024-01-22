from app import app

# Erstellen der Flask-Anwendung


if __name__ == '__main__':
    app.config.from_object('config.DevelopmentConfig')  # Für Entwicklungszwecke
    # app.config.from_object('config.ProductionConfig')  # Für Produktionszwecke

    app.run(debug=True, port=8020, use_reloader=False)