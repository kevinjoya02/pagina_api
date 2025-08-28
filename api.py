import datetime
import holidays
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

#BASE DE DATOS
productos = {
'camisas': [
    {"id": 1, "nombre": "Camisa Luna", "descripcion": "Camisa de lino fresca ideal para verano.", "precio": 32.99, "imagen": "/static/imagenes/camisa1.jpg"},
    {"id": 2, "nombre": "Camisa Eco", "descripcion": "Hecha con algodón orgánico, suave al tacto.", "precio": 29.50, "imagen": "/static/imagenes/camisa2.jpg"},
    {"id": 3, "nombre": "Camisa Nórdica", "descripcion": "Estilo escandinavo con corte minimalista.", "precio": 34.90, "imagen": "/static/imagenes/camisa1.jpg"},
    {"id": 4, "nombre": "Camisa Terra", "descripcion": "Tonos tierra, perfecta para outfits relajados.", "precio": 31.00, "imagen": "/static/imagenes/camisa2.jpg"},
    {"id": 5, "nombre": "Camisa Vintage", "descripcion": "Diseño retro con cuello abierto.", "precio": 27.75, "imagen": "/static/imagenes/camisa1.jpg"},
    {"id": 6, "nombre": "Camisa Cielo", "descripcion": "Color celeste con botones de madera.", "precio": 36.40, "imagen": "/static/imagenes/camisa2.jpg"},
    {"id": 7, "nombre": "Camisa Urbana", "descripcion": "Estilo moderno para uso en la ciudad.", "precio": 33.25, "imagen": "/static/imagenes/camisa1.jpg"},
    {"id": 8, "nombre": "Camisa Brisa", "descripcion": "Tejido ligero para climas cálidos.", "precio": 28.60, "imagen": "/static/imagenes/camisa2.jpg"},
    {"id": 9, "nombre": "Camisa Aurora", "descripcion": "Diseño con tonos pasteles degradados.", "precio": 30.80, "imagen": "/static/imagenes/camisa1.jpg"},
    {"id": 10, "nombre": "Camisa Zen", "descripcion": "Corte relajado y estilo minimalista.", "precio": 35.00, "imagen": "/static/imagenes/camisa2.jpg"},
],
'pantalones': [
    {"id": 1, "nombre": "Pantalón Andes", "descripcion": "Jeans azul clásico, resistentes y cómodos.", "precio": 42.99, "imagen": "/static/imagenes/pantalon1.jpg"},
    {"id": 2, "nombre": "Pantalón EcoFit", "descripcion": "Confeccionado con algodón reciclado, flexible y moderno.", "precio": 39.50, "imagen": "/static/imagenes/pantalon2.jpg"},
    {"id": 3, "nombre": "Pantalón Nórdico", "descripcion": "Estilo slim fit inspirado en diseño escandinavo.", "precio": 44.90, "imagen": "/static/imagenes/pantalon1.jpg"},
    {"id": 4, "nombre": "Pantalón Terra", "descripcion": "Tonos beige y tierra, ideal para looks casuales.", "precio": 41.00, "imagen": "/static/imagenes/pantalon2.jpg"},
    {"id": 5, "nombre": "Pantalón Retro", "descripcion": "Estilo vintage con corte ancho y bolsillos grandes.", "precio": 37.75, "imagen": "/static/imagenes/pantalon1.jpg"},
    {"id": 6, "nombre": "Pantalón Cielo", "descripcion": "Color celeste con tela ligera y fresca.", "precio": 46.40, "imagen": "/static/imagenes/pantalon2.jpg"},
    {"id": 7, "nombre": "Pantalón Urbano", "descripcion": "Diseño moderno, perfecto para outfits streetwear.", "precio": 43.25, "imagen": "/static/imagenes/pantalon1.jpg"},
    {"id": 8, "nombre": "Pantalón Brisa", "descripcion": "Tejido transpirable para climas cálidos.", "precio": 38.60, "imagen": "/static/imagenes/pantalon2.jpg"},
    {"id": 9, "nombre": "Pantalón Aurora", "descripcion": "Colores degradados con diseño innovador.", "precio": 40.80, "imagen": "/static/imagenes/pantalon1.jpg"},
    {"id": 10, "nombre": "Pantalón Zen", "descripcion": "Corte relajado y minimalista para comodidad total.", "precio": 45.00, "imagen": "/static/imagenes/pantalon2.jpg"},
],
'camisetas': [
    {"id": 1, "nombre": "Camiseta Clásica", "descripcion": "Básica de algodón, ideal para cualquier ocasión.", "precio": 19.90, "imagen": "/static/imagenes/camiseta1.jpg"},
    {"id": 2, "nombre": "Camiseta Sport", "descripcion": "Tela transpirable para entrenamientos y uso diario.", "precio": 22.50, "imagen": "/static/imagenes/camiseta2.jpg"},
    {"id": 3, "nombre": "Camiseta Urbana", "descripcion": "Estilo moderno con estampado gráfico.", "precio": 24.30, "imagen": "/static/imagenes/camiseta1.jpg"},
    {"id": 4, "nombre": "Camiseta Retro", "descripcion": "Diseño inspirado en los años 90.", "precio": 21.70, "imagen": "/static/imagenes/camiseta2.jpg"},
    {"id": 5, "nombre": "Camiseta Eco", "descripcion": "Hecha con algodón reciclado y amigable con el ambiente.", "precio": 23.90, "imagen": "/static/imagenes/camiseta1.jpg"},
    {"id": 6, "nombre": "Camiseta Minimal", "descripcion": "Diseño limpio con corte relajado.", "precio": 20.80, "imagen": "/static/imagenes/camiseta2.jpg"},
    {"id": 7, "nombre": "Camiseta Viajera", "descripcion": "Ligera y cómoda para días de aventura.", "precio": 25.40, "imagen": "/static/imagenes/camiseta1.jpg"},
    {"id": 8, "nombre": "Camiseta Nocturna", "descripcion": "Negra con detalles brillantes discretos.", "precio": 26.10, "imagen": "/static/imagenes/camiseta2.jpg"},
    {"id": 9, "nombre": "Camiseta ColorMix", "descripcion": "Estampado multicolor que resalta tu estilo.", "precio": 27.00, "imagen": "/static/imagenes/camiseta1.jpg"},
    {"id": 10, "nombre": "Camiseta Zen", "descripcion": "Inspirada en la tranquilidad y lo natural.", "precio": 22.90, "imagen": "/static/imagenes/camiseta2.jpg"},
],
'blusas': [
    {"id": 1, "nombre": "Blusa Encanto", "descripcion": "Blusa de seda ligera con caída elegante.", "precio": 32.50, "imagen": "/static/imagenes/blusa1.jpg"},
    {"id": 2, "nombre": "Blusa Primavera", "descripcion": "Estampado floral colorido, ideal para el día.", "precio": 28.40, "imagen": "/static/imagenes/blusa2.jpg"},
    {"id": 3, "nombre": "Blusa Perla", "descripcion": "Color blanco perlado con detalles delicados en el cuello.", "precio": 34.20, "imagen": "/static/imagenes/blusa1.jpg"},
    {"id": 4, "nombre": "Blusa Elegancia Negra", "descripcion": "Blusa negra de manga larga con botones dorados.", "precio": 36.80, "imagen": "/static/imagenes/blusa2.jpg"},
    {"id": 5, "nombre": "Blusa Casual Denim", "descripcion": "Estilo mezclilla con corte moderno y fresco.", "precio": 30.90, "imagen": "/static/imagenes/blusa1.jpg"},
    {"id": 6, "nombre": "Blusa Cielo", "descripcion": "Color celeste con detalles plisados en el frente.", "precio": 27.60, "imagen": "/static/imagenes/blusa2.jpg"},
    {"id": 7, "nombre": "Blusa Tropical", "descripcion": "Colores vibrantes y tela fresca para verano.", "precio": 29.95, "imagen": "/static/imagenes/blusa1.jpg"},
    {"id": 8, "nombre": "Blusa Nocturna", "descripcion": "Estilo elegante con transparencias sutiles.", "precio": 38.10, "imagen": "/static/imagenes/blusa2.jpg"},
    {"id": 9, "nombre": "Blusa Arena", "descripcion": "Tono beige con bordados artesanales.", "precio": 33.40, "imagen": "/static/imagenes/blusa1.jpg"},
    {"id": 10, "nombre": "Blusa Romántica", "descripcion": "Detalles de encaje y mangas abullonadas.", "precio": 35.20, "imagen": "/static/imagenes/blusa2.jpg"},
],
}

#festivos de colombia 
colombia_holidays = holidays.CO(years=datetime.datetime.now().year)
def siguiente_dia_habil(fecha):
    while fecha.weekday() >= 5 or fecha in colombia_holidays:
        fecha += datetime.timedelta(days=1)
    return fecha

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/fecha_entrega')
def fecha_entrega():
    hoy = datetime.date(2025,9,2)
    fecha = siguiente_dia_habil(hoy)
    return jsonify({"fecha_entrega": fecha.strftime("%A %d-%m-%Y")})

#obtener categorias
@app.route('/api/productos/<categoria>')
def obtener_productos(categoria):
    cat = categoria.lower()
    if cat in productos:
        return jsonify(productos[cat])
    else:
        return jsonify({"error": "categoria no encontrada"}), 404

@app.route('/api/productos/<categoria>/<int:producto_id>', methods = ['DELETE'])
def elminar_producto(categoria,producto_id):
    cat = categoria.lower()
    if cat in productos:
        lista = productos[cat]
        for p in lista:
            if p['id'] == producto_id:
                lista.remove(p)
                return jsonify({"mensaje": f"Producto {producto_id} eliminado de {categoria}"}), 200
        return jsonify({"error": "Producto no encontrado"}), 404
    else:
        return jsonify({"error": "Categoría no encontrada"}), 404
    


if __name__ == '__main__':
    app.run(debug=True)