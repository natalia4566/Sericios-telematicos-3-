import os
from flask import Flask
from users.models.db import db

from web.views import web_bp
from users.controllers.user_controller import user_controller
from products import products_bp

app = Flask(
    __name__,
    template_folder='web/templates',
    static_folder='web/static'
)

# Leer DB desde docker-compose
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db.init_app(app)

# Registrar blueprints
app.register_blueprint(web_bp)
app.register_blueprint(user_controller)
app.register_blueprint(products_bp)

# Crear tablas
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

