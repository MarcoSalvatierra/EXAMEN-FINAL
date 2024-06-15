from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from Entity import Aeropuertos, Vuelos, Pasajeros, Asientos, Reservas, Base
from datetime import datetime

app = Flask(__name__)
app.secret_key = '123456'

# Crear conexión a la base de datos
engine = create_engine('postgresql://postgres:123456@localhost/vuelo')
Base.metadata.bind = engine

# Crear sesión de base de datos
DBSession = sessionmaker(bind=engine)

# Ruta Principal
@app.route('/')
def home():
    return render_template('index.html')

# Listar aeropuertos
@app.route('/aeropuertos')
def listar_aeropuertos():
    session = DBSession()
    aeropuertos = session.query(Aeropuertos).all()
    session.close()
    return render_template('aeropuertos.html', aeropuertos=aeropuertos)

# Agregar aeropuerto
@app.route('/aeropuertos/agregar', methods=['GET', 'POST'])
def agregar_aeropuerto():
    if request.method == 'POST':
        try:
            session = DBSession()
            aeropuerto = Aeropuertos(codigo_aeropuerto=request.form['codigo_aeropuerto'],
                                     nombre=request.form['nombre'],
                                     ciudad=request.form['ciudad'],
                                     pais=request.form['pais'])
            session.add(aeropuerto)
            session.commit()
            flash('Aeropuerto agregado correctamente', 'success')
            session.close()
            return redirect(url_for('listar_aeropuertos'))
        except IntegrityError as e:
            session.rollback()
            flash('Error: El código de aeropuerto ya existe', 'error')
        except Exception as e:
            session.rollback()
            flash(f'Error al agregar aeropuerto: {e}', 'error')
    return render_template('agregar_aeropuerto.html')

# Listar vuelos
@app.route('/vuelos')
def listar_vuelos():
    session = DBSession()
    vuelos = session.query(Vuelos).all()
    session.close()
    return render_template('vuelos.html', vuelos=vuelos)

# Agregar vuelo
@app.route('/vuelos/agregar', methods=['GET', 'POST'])
def agregar_vuelo():
    if request.method == 'POST':
        try:
            session = DBSession()
            vuelo = Vuelos(numero_vuelo=request.form['numero_vuelo'],
                           origen=request.form['origen'],
                           destino=request.form['destino'],
                           fecha=datetime.strptime(request.form['fecha'], '%Y-%m-%d').date(),
                           hora_salida=datetime.strptime(request.form['hora_salida'], '%H:%M').time(),
                           hora_llegada=datetime.strptime(request.form['hora_llegada'], '%H:%M').time(),
                           estado=request.form['estado'])
            session.add(vuelo)
            session.commit()
            flash('Vuelo agregado correctamente', 'success')
            session.close()
            return redirect(url_for('listar_vuelos'))
        except IntegrityError as e:
            session.rollback()
            flash('Error: El número de vuelo ya existe', 'error')
        except Exception as e:
            session.rollback()
            flash(f'Error al agregar vuelo: {e}', 'error')
    return render_template('agregar_vuelo.html')

if __name__ == '__main__':
    app.run(debug=True)
