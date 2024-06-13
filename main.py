from flask import Flask, render_template, make_response, redirect, url_for
from datetime import datetime, timedelta
import time

app = Flask(__name__)

# Función para verificar si se alcanzó la fecha objetivo
def verificar_fecha(fecha_objetivo):
    return datetime.now() >= fecha_objetivo

# Endpoint de error 404
@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('error.html', error=error)

# Endpoint index con el contador regresivo
@app.route('/index')
def index():
    fecha_objetivo = datetime(2026, 7, 11, 14, 30, 0)  # Establece la fecha y hora objetivo
    if verificar_fecha(fecha_objetivo):
        return redirect(url_for('tiempo_completado'))
    else:
        tiempo_restante = fecha_objetivo - datetime.now()
        tiempo_restante_segundos = int(tiempo_restante.total_seconds())
        return render_template("index.html", tiempo_restante=tiempo_restante_segundos)

#Endpoint para cuando se complete el tiempo
@app.route('/completado')
def tiempo_completado():
    fecha_objetivo = datetime(2026, 7, 11, 14, 30, 0)  # Establece la fecha y hora objetivo
    if verificar_fecha(fecha_objetivo):
        return render_template("completado.html")
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
