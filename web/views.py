from flask import Blueprint, render_template, jsonify, request
from web.models.producto import Producto
from users.models.db import db

# --- Definir el blueprint ---
web_bp = Blueprint('web_bp', __name__)

# --- Rutas de vistas ---
@web_bp.route('/')
def index():
    return render_template('index.html')

@web_bp.route('/edit/<string:id>')
def edit_user(id):
    print("id recibido", id)
    return render_template('edit.html', id=id)

# --- Rutas de productos ---
@web_bp.route('/api/productos', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    data = [
        {
            'id': p.id,
            'nombre': p.nombre,
            'descripcion': p.descripcion,
            'precio': p.precio
        }
        for p in productos
    ]
    return jsonify(data)

@web_bp.route('/api/productos', methods=['POST'])
def add_producto():
    data = request.get_json()
    nuevo = Producto(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        precio=data['precio']
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'mensaje': 'Producto agregado correctamente'}), 201

