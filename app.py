from flask import Flask, render_template_string

app = Flask(__name__)

# Diseñamos el menú en HTML
MENU_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Menú Flask</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; text-align: center; padding: 20px; }
        .menu-card { background: white; max-width: 400px; margin: 0 auto; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        h1 { color: #ff5722; }
        .item { display: flex; justify-content: space-between; margin: 15px 0; border-bottom: 1px dashed #ccc; padding-bottom: 5px; }
        .precio { font-weight: bold; color: #2e7d32; }
    </style>
</head>
<body>
    <div class="menu-card">
        <h1>Bistro Flask</h1>
        <p><i>Menú desde un contenedor Python</i></p>
        <hr>
        <div class="item"><span>🍔 Hamburguesa</span><span class="precio">$8.50</span></div>
        <div class="item"><span>🍕 Pizza</span><span class="precio">$10.00</span></div>
        <div class="item"><span>🥗 Ensalada</span><span class="precio">$6.00</span></div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(MENU_HTML)

if __name__ == '__main__':
    # Corremos en el puerto 5000 y permitimos conexiones externas
    app.run(host='0.0.0.0', port=5000)