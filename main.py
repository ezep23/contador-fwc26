from flask import Flask, render_template, make_response, redirect, url_for
from datetime import datetime, timedelta
import time

app = Flask(__name__)

@app.route('/index')
def index():
    fecha_objetivo = datetime(2026, 7, 11, 14, 30, 0)  # Establece la fecha y hora objetivo
    while datetime.now() < fecha_objetivo:
        tiempo_restante = fecha_objetivo - datetime.now()
        tiempo_restante_segundos = tiempo_restante.total_seconds()
        return render_template("index.html", tiempo_restante=tiempo_restante_segundos)
        time.sleep(1)  # Espera 1 segundo antes de volver a verificar
    return redirect(url_for('/tcompletado'))

@app.route('/tcompletado')
def tiempo_completado():
    return "¡Tiempo completado!"

if __name__ == '__main__':
    app.run(debug=True)
