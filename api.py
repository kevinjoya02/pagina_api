from flask import Flask, jsonify, request
app = Flask(__name__)

#BASE DE DATOS
productos = {
    'camisas':[
        {"id": 1, "nombre": "CamisAAAAAA", "descripcion": "Camisa elegante para oficina.", "precio": 25.00, "imagen": "https://via.placeholder.com/150?text=Camisa+1"},
        {"id": 2, "nombre": "Camisa 2", "descripcion": "Camisa casual para uso diario.", "precio": 20.00, "imagen": "https://via.placeholder.com/150?text=Camisa+2"},
        {"id": 3, "nombre": "Camisa 3", "descripcion": "Camisa formal de algodón.", "precio": 30.00, "imagen": "https://via.placeholder.com/150?text=Camisa+3"},
        {"id": 4, "nombre": "Camisa 4", "descripcion": "Camisa con estampado moderno.", "precio": 27.00, "imagen": "https://via.placeholder.com/150?text=Camisa+4"},
        {"id": 5, "nombre": "Camisa 5", "descripcion": "Camisa deportiva ligera.", "precio": 22.00, "imagen": "https://via.placeholder.com/150?text=Camisa+5"},
        {"id": 6, "nombre": "Camisa 6", "descripcion": "Camisa elegante de seda.", "precio": 40.00, "imagen": "https://via.placeholder.com/150?text=Camisa+6"},
        {"id": 7, "nombre": "Camisa 7", "descripcion": "Camisa casual de lino.", "precio": 28.00, "imagen": "https://via.placeholder.com/150?text=Camisa+7"},
        {"id": 8, "nombre": "Camisa 8", "descripcion": "Camisa de manga larga.", "precio": 26.00, "imagen": "https://via.placeholder.com/150?text=Camisa+8"},
        {"id": 9, "nombre": "Camisa 9", "descripcion": "Camisa deportiva con ventilación.", "precio": 24.00, "imagen": "https://via.placeholder.com/150?text=Camisa+9"},
        {"id": 10, "nombre": "Camisa 10", "descripcion": "Camisa casual moderna.", "precio": 23.00, "imagen": "https://via.placeholder.com/150?text=Camisa+10"},
    ],
        'pantalones':[
        {"id": 1, "nombre": "pantalones 1", "descripcion": "Camisa elegante para oficina.", "precio": 25.00, "imagen": "https://via.placeholder.com/150?text=Camisa+1"},
        {"id": 2, "nombre": "pantalones 2", "descripcion": "Camisa casual para uso diario.", "precio": 20.00, "imagen": "https://via.placeholder.com/150?text=Camisa+2"},
        {"id": 3, "nombre": "Camisa 3", "descripcion": "Camisa formal de algodón.", "precio": 30.00, "imagen": "https://via.placeholder.com/150?text=Camisa+3"},
        {"id": 4, "nombre": "Camisa 4", "descripcion": "Camisa con estampado moderno.", "precio": 27.00, "imagen": "https://via.placeholder.com/150?text=Camisa+4"},
        {"id": 5, "nombre": "Camisa 5", "descripcion": "Camisa deportiva ligera.", "precio": 22.00, "imagen": "https://via.placeholder.com/150?text=Camisa+5"},
        {"id": 6, "nombre": "Camisa 6", "descripcion": "Camisa elegante de seda.", "precio": 40.00, "imagen": "https://via.placeholder.com/150?text=Camisa+6"},
        {"id": 7, "nombre": "Camisa 7", "descripcion": "Camisa casual de lino.", "precio": 28.00, "imagen": "https://via.placeholder.com/150?text=Camisa+7"},
        {"id": 8, "nombre": "Camisa 8", "descripcion": "Camisa de manga larga.", "precio": 26.00, "imagen": "https://via.placeholder.com/150?text=Camisa+8"},
        {"id": 9, "nombre": "Camisa 9", "descripcion": "Camisa deportiva con ventilación.", "precio": 24.00, "imagen": "https://via.placeholder.com/150?text=Camisa+9"},
        {"id": 10, "nombre": "Camisa 10", "descripcion": "Camisa casual moderna.", "precio": 23.00, "imagen": "https://via.placeholder.com/150?text=Camisa+10"},
    ],    'ccamisetas':[
        {"id": 1, "nombre": "Camisa 1", "descripcion": "Camisa elegante para oficina.", "precio": 25.00, "imagen": "https://via.placeholder.com/150?text=Camisa+1"},
        {"id": 2, "nombre": "Camisa 2", "descripcion": "Camisa casual para uso diario.", "precio": 20.00, "imagen": "https://via.placeholder.com/150?text=Camisa+2"},
        {"id": 3, "nombre": "Camisa 3", "descripcion": "Camisa formal de algodón.", "precio": 30.00, "imagen": "https://via.placeholder.com/150?text=Camisa+3"},
        {"id": 4, "nombre": "Camisa 4", "descripcion": "Camisa con estampado moderno.", "precio": 27.00, "imagen": "https://via.placeholder.com/150?text=Camisa+4"},
        {"id": 5, "nombre": "Camisa 5", "descripcion": "Camisa deportiva ligera.", "precio": 22.00, "imagen": "https://via.placeholder.com/150?text=Camisa+5"},
        {"id": 6, "nombre": "Camisa 6", "descripcion": "Camisa elegante de seda.", "precio": 40.00, "imagen": "https://via.placeholder.com/150?text=Camisa+6"},
        {"id": 7, "nombre": "Camisa 7", "descripcion": "Camisa casual de lino.", "precio": 28.00, "imagen": "https://via.placeholder.com/150?text=Camisa+7"},
        {"id": 8, "nombre": "Camisa 8", "descripcion": "Camisa de manga larga.", "precio": 26.00, "imagen": "https://via.placeholder.com/150?text=Camisa+8"},
        {"id": 9, "nombre": "Camisa 9", "descripcion": "Camisa deportiva con ventilación.", "precio": 24.00, "imagen": "https://via.placeholder.com/150?text=Camisa+9"},
        {"id": 10, "nombre": "Camisa 10", "descripcion": "Camisa casual moderna.", "precio": 23.00, "imagen": "https://via.placeholder.com/150?text=Camisa+10"},
    ],    'blusas':[
        {"id": 1, "nombre": "Camisa 1", "descripcion": "Camisa elegante para oficina.", "precio": 25.00, "imagen": "https://via.placeholder.com/150?text=Camisa+1"},
        {"id": 2, "nombre": "Camisa 2", "descripcion": "Camisa casual para uso diario.", "precio": 20.00, "imagen": "https://via.placeholder.com/150?text=Camisa+2"},
        {"id": 3, "nombre": "Camisa 3", "descripcion": "Camisa formal de algodón.", "precio": 30.00, "imagen": "https://via.placeholder.com/150?text=Camisa+3"},
        {"id": 4, "nombre": "Camisa 4", "descripcion": "Camisa con estampado moderno.", "precio": 27.00, "imagen": "https://via.placeholder.com/150?text=Camisa+4"},
        {"id": 5, "nombre": "Camisa 5", "descripcion": "Camisa deportiva ligera.", "precio": 22.00, "imagen": "https://via.placeholder.com/150?text=Camisa+5"},
        {"id": 6, "nombre": "Camisa 6", "descripcion": "Camisa elegante de seda.", "precio": 40.00, "imagen": "https://via.placeholder.com/150?text=Camisa+6"},
        {"id": 7, "nombre": "Camisa 7", "descripcion": "Camisa casual de lino.", "precio": 28.00, "imagen": "https://via.placeholder.com/150?text=Camisa+7"},
        {"id": 8, "nombre": "Camisa 8", "descripcion": "Camisa de manga larga.", "precio": 26.00, "imagen": "https://via.placeholder.com/150?text=Camisa+8"},
        {"id": 9, "nombre": "Camisa 9", "descripcion": "Camisa deportiva con ventilación.", "precio": 24.00, "imagen": "https://via.placeholder.com/150?text=Camisa+9"},
        {"id": 10, "nombre": "Camisa 10", "descripcion": "Camisa casual moderna.", "precio": 23.00, "imagen": "https://via.placeholder.com/150?text=Camisa+10"},
    ],
}

#obtener categorias
@app.route('/api/productos/<categoria>')
def obtener_productos(categoria):
    cat = categoria.lower()
    if cat in productos:
        return jsonify(productos[cat])
    else:
        return jsonify({"error": "categoria no encontrada"}), 404
    

if __name__ == '__main__':
    app.run(debug=True)