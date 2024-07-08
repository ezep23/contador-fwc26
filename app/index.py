# Importamos el paquete predeterminado de tiempo de python 
from datetime import datetime, time, timedelta
# Importamos el framework de Flask
from flask import Flask, render_template, make_response, redirect, url_for, jsonify

app = Flask(__name__)

# Función para verificar si se alcanzó la fecha objetivo
def verificar_fecha(fecha_objetivo):
    return datetime.now() >= fecha_objetivo

# Endpoint index con el contador regresivo
@app.route('/')
def index():
    return render_template('index.html')

#Endpoint para cuando se complete el tiempo
@app.route('/completado')
def tiempo_completado():
    fecha_objetivo = datetime(2026, 7, 11, 14, 30, 0)  # Establece la fecha y hora objetivo
    if verificar_fecha(fecha_objetivo):
        return render_template('completado.html')
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
