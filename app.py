from flask import Flask, render_template_string

app = Flask(__name__)

# Datos del menú organizados de forma limpia en Python
MENU_DATA = {
    "restaurante": "Bistro Gourmet",
    "eslogan": "Sabor artesanal en cada plato",
    "categorias": {
        "Platos Fuertes": [
            {"icono": "🍔", "nombre": "Hamburguesa Premium", "desc": "Carne Angus, queso cheddar, tocino crujiente y salsa de la casa.", "precio": 12.50},
            {"icono": "🍕", "nombre": "Pizza Pepperoni Especial", "desc": "Masa madre, salsa de tomate artesanal y doble queso mozzarella.", "precio": 14.00},
            {"icono": "🥗", "nombre": "Ensalada Avocato", "desc": "Mix de verdes, aguacate, tomates cherry, pollo a la plancha y aderezo.", "precio": 9.50}
        ],
        "Bebidas & Postres": [
            {"icono": "🥤", "nombre": "Limonada Imperial", "desc": "Hierbabuena fresca y endulzada con miel natural.", "precio": 3.50},
            {"icono": "🍰", "nombre": "Cheesecake de Frutos Rojos", "desc": "Receta clásica con una base crocante de galleta.", "precio": 5.00}
        ]
    }
}

# Diseño HTML y CSS moderno integrado
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menú - {{ data.restaurante }}</title>
    <style>
        :root {
            --bg-color: #f8fafc;
            --card-bg: #ffffff;
            --primary-color: #e28743;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --price-color: #10b981;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0;
            padding: 40px 20px;
        }

        .container {
            max-width: 500px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
        }

        .header h1 {
            font-size: 2.5rem;
            margin: 0 0 10px 0;
            color: var(--text-main);
            font-weight: 800;
        }

        .header p {
            color: var(--primary-color);
            font-style: italic;
            margin: 0;
            font-size: 1.1rem;
        }

        .category-title {
            font-size: 1.25rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin: 30px 0 15px 0;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 5px;
        }

        .menu-item {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            display: flex;
            align-items: flex-start;
            gap: 15px;
            transition: transform 0.2s ease;
        }

        .menu-item:hover {
            transform: translateY(-2px);
        }

        .item-icon {
            font-size: 2rem;
            background: #fff7ed;
            padding: 8px;
            border-radius: 10px;
        }

        .item-details {
            flex-grow: 1;
        }

        .item-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 5px;
        }

        .item-name {
            font-weight: 700;
            font-size: 1.1rem;
        }

        .item-price {
            font-weight: 700;
            color: var(--price-color);
            font-size: 1.1rem;
        }

        .item-desc {
            color: var(--text-muted);
            font-size: 0.9rem;
            line-height: 1.4;
            margin: 0;
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="header">
            <h1>{{ data.restaurante }}</h1>
            <p>{{ data.eslogan }}</p>
        </div>

        {% for categoria, platos in data.categorias.items() %}
            <div class="category-title">{{ categoria }}</div>
            
            {% for plato in platos %}
                <div class="menu-item">
                    <div class="item-icon">{{ plato.icono }}</div>
                    <div class="item-details">
                        <div class="item-header">
                            <span class="item-name">{{ plato.nombre }}</span>
                            <span class="item-price">${{ "%.2f"|format(plato.precio) }}</span>
                        </div>
                        <p class="item-desc">{{ plato.desc }}</p>
                    </div>
                </div>
            {% endfor %}
        {% endfor %}
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, data=MENU_DATA)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)