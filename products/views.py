from flask import render_template
from . import products_bp

@products_bp.route('/productos')
def productos():
    productos = [
        {"id": 1, "nombre": "Bolso artesanal", "precio": 85000},
        {"id": 2, "nombre": "Bolso de cuero", "precio": 120000},
        {"id": 3, "nombre": "Mochila urbana", "precio": 95000},
        {"id": 4, "nombre": "Bolso de tela reciclada", "precio": 78000},
        {"id": 5, "nombre": "Bolso playero", "precio": 67000},
    ]
    return render_template('productos.html', productos=productos)

