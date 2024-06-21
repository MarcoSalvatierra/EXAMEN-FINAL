from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
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
    session = DBSession()
    aeropuertos = session.query(Aeropuertos).all()
    session.close()

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

    return render_template('agregar_vuelo.html', aeropuertos=aeropuertos)

@app.route('/vuelos/modificar/<string:numero_vuelo>', methods=['GET', 'POST'])
def modificar_vuelo(numero_vuelo):
    session = DBSession()
    vuelo = session.query(Vuelos).filter_by(numero_vuelo=numero_vuelo).first()

    if request.method == 'POST':
        try:
            vuelo.origen = request.form['origen']
            vuelo.destino = request.form['destino']
            vuelo.fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d').date()
            vuelo.hora_salida = datetime.strptime(request.form['hora_salida'], '%H:%M').time()
            vuelo.hora_llegada = datetime.strptime(request.form['hora_llegada'], '%H:%M').time()
            vuelo.estado = request.form['estado']

            session.commit()
            flash('Vuelo modificado correctamente', 'success')
            return redirect(url_for('listar_vuelos'))
        except IntegrityError as e:
            session.rollback()
            flash('Error: El número de vuelo ya existe', 'error')
        except Exception as e:
            session.rollback()
            flash(f'Error al modificar vuelo: {e}', 'error')
        finally:
            session.close()

    aeropuertos = session.query(Aeropuertos).all()
    session.close()
    return render_template('modificar_vuelo.html', vuelo=vuelo, aeropuertos=aeropuertos)

@app.route('/vuelos/eliminar/<string:numero_vuelo>', methods=['POST'])
def eliminar_vuelo(numero_vuelo):
    session = DBSession()
    try:
        vuelo = session.query(Vuelos).filter_by(numero_vuelo=numero_vuelo).first()
        if vuelo:
            session.delete(vuelo)
            session.commit()
            flash('Vuelo eliminado correctamente', 'success')
        else:
            flash('Vuelo no encontrado', 'error')
    except Exception as e:
        session.rollback()
        flash(f'Error al eliminar vuelo: {e}', 'error')
    finally:
        session.close()
    
    return redirect(url_for('listar_vuelos'))

# Listar pasajeros
@app.route('/pasajeros')
def listar_pasajeros():
    session = DBSession()
    pasajeros = session.query(Pasajeros).all()
    session.close()
    return render_template('pasajeros.html', pasajeros=pasajeros)

# Agregar pasajero
@app.route('/pasajeros/agregar', methods=['GET', 'POST'])
def agregar_pasajero():
    if request.method == 'POST':
        try:
            session = DBSession()
            pasajero = Pasajeros(nombre=request.form['nombre'],
                                 apellido=request.form['apellido'],
                                 email=request.form['email'],
                                 telefono=request.form['telefono'])
            session.add(pasajero)
            session.commit()
            flash('Pasajero agregado correctamente', 'success')
            session.close()
            return redirect(url_for('listar_pasajeros'))
        except IntegrityError as e:
            session.rollback()
            flash('Error: El pasajero ya existe', 'error')
        except Exception as e:
            session.rollback()
            flash(f'Error al agregar pasajero: {e}', 'error')
    return render_template('agregar_pasajero.html')

# Modificar pasajero
@app.route('/pasajeros/modificar/<int:id_pasajero>', methods=['GET', 'POST'])
def modificar_pasajero(id_pasajero):
    session = DBSession()
    pasajero = session.query(Pasajeros).filter_by(id_pasajero=id_pasajero).first()

    if request.method == 'POST':
        try:
            pasajero.nombre = request.form['nombre']
            pasajero.apellido = request.form['apellido']
            pasajero.email = request.form['email']
            pasajero.telefono = request.form['telefono']
            session.commit()
            flash('Pasajero modificado correctamente', 'success')
            session.close()
            return redirect(url_for('listar_pasajeros'))
        except IntegrityError as e:
            session.rollback()
            flash('Error: El pasajero ya existe', 'error')
        except Exception as e:
            session.rollback()
            flash(f'Error al modificar pasajero: {e}', 'error')

    return render_template('modificar_pasajero.html', pasajero=pasajero)

# Eliminar pasajero
@app.route('/pasajeros/eliminar/<int:id_pasajero>', methods=['POST'])
def eliminar_pasajero(id_pasajero):
    session = DBSession()
    pasajero = session.query(Pasajeros).filter_by(id_pasajero=id_pasajero).first()

    try:
        session.delete(pasajero)
        session.commit()
        flash('Pasajero eliminado correctamente', 'success')
    except Exception as e:
        session.rollback()
        flash(f'Error al eliminar pasajero: {e}', 'error')
    finally:
        session.close()

    return redirect(url_for('listar_pasajeros'))

@app.route('/asientos')
def listar_asientos():
    session = DBSession()
    asientos = session.query(Asientos).all()
    session.close()
    return render_template('asientos.html', asientos=asientos)

@app.route('/asientos/agregar', methods=['GET', 'POST'])
def agregar_asiento():
    if request.method == 'POST':
        try:
            session = DBSession()
            asiento = Asientos(
                numero_vuelo=request.form['numero_vuelo'],
                numero_asiento=request.form['numero_asiento'],
                clase=request.form['clase'],
                disponible=True  # Por defecto, un asiento nuevo está disponible
            )
            session.add(asiento)
            session.commit()
            flash('Asiento agregado correctamente', 'success')
            session.close()
            return redirect(url_for('listar_asientos'))
        except IntegrityError as e:
            session.rollback()
            flash('Error: No se pudo agregar el asiento', 'error')
        except Exception as e:
            session.rollback()
            flash(f'Error al agregar asiento: {e}', 'error')
    session = DBSession()
    vuelos = session.query(Vuelos).all()
    session.close()
    return render_template('agregar_asiento.html', vuelos=vuelos)


@app.route('/asientos/modificar/<int:id_asiento>', methods=['GET', 'POST'])
def modificar_asiento(id_asiento):
    session = DBSession()
    asiento = session.query(Asientos).filter_by(id_asiento=id_asiento).one()
    vuelos = session.query(Vuelos).all()
    if request.method == 'POST':
        try:
            asiento.numero_vuelo = request.form['numero_vuelo']
            asiento.numero_asiento = request.form['numero_asiento']
            asiento.clase = request.form['clase']
            asiento.disponible = 'disponible' in request.form
            session.commit()
            flash('Asiento modificado correctamente', 'success')
            session.close()
            return redirect(url_for('listar_asientos'))
        except Exception as e:
            session.rollback()
            flash(f'Error al modificar asiento: {e}', 'error')
    session.close()
    return render_template('modificar_asiento.html', asiento=asiento, vuelos=vuelos)

@app.route('/asientos/eliminar/<int:id_asiento>', methods=['POST'])
def eliminar_asiento(id_asiento):
    session = DBSession()
    try:
        asiento = session.query(Asientos).filter_by(id_asiento=id_asiento).one()
        session.delete(asiento)
        session.commit()
        flash('Asiento eliminado correctamente', 'success')
    except Exception as e:
        session.rollback()
        flash(f'Error al eliminar asiento: {e}', 'error')
    session.close()
    return redirect(url_for('listar_asientos'))

@app.route('/reservas')
def listar_reservas():
    session = DBSession()
    # Utiliza joinedload para cargar el pasajero y el asiento de la reserva en la misma consulta
    reservas = session.query(Reservas).options(joinedload(Reservas.pasajero), joinedload(Reservas.asiento)).all()
    session.close()
    return render_template('reservas.html', reservas=reservas)

@app.route('/reservas/agregar', methods=['GET', 'POST'])
def agregar_reserva():
    if request.method == 'POST':
        try:
            session = DBSession()
            reserva = Reservas(
                id_pasajero=request.form['id_pasajero'],
                id_asiento=request.form['id_asiento'],
                fecha_reserva=datetime.strptime(request.form['fecha_reserva'], '%Y-%m-%d').date(),
                estado=request.form['estado']
            )
            session.add(reserva)
            session.commit()
            flash('Reserva agregada correctamente', 'success')
            session.close()
            return redirect(url_for('listar_reservas'))
        except IntegrityError as e:
            session.rollback()
            flash('Error: No se pudo agregar la reserva', 'error')
        except Exception as e:
            session.rollback()
            flash(f'Error al agregar reserva: {e}', 'error')
    session = DBSession()
    pasajeros = session.query(Pasajeros).all()
    asientos = session.query(Asientos).filter_by(disponible=True).all()
    session.close()
    return render_template('agregar_reserva.html', pasajeros=pasajeros, asientos=asientos)

@app.route('/reservas/modificar/<int:id_reserva>', methods=['GET', 'POST'])
def modificar_reserva(id_reserva):
    session = DBSession()
    reserva = session.query(Reservas).filter_by(id_reserva=id_reserva).one()
    pasajeros = session.query(Pasajeros).all()
    asientos = session.query(Asientos).filter_by(disponible=True).all()
    if request.method == 'POST':
        try:
            reserva.id_pasajero = request.form['id_pasajero']
            reserva.id_asiento = request.form['id_asiento']
            reserva.fecha_reserva = datetime.strptime(request.form['fecha_reserva'], '%Y-%m-%d').date()
            reserva.estado = request.form['estado']
            session.commit()
            flash('Reserva modificada correctamente', 'success')
            session.close()
            return redirect(url_for('listar_reservas'))
        except Exception as e:
            session.rollback()
            flash(f'Error al modificar reserva: {e}', 'error')
    session.close()
    return render_template('modificar_reserva.html', reserva=reserva, pasajeros=pasajeros, asientos=asientos)

@app.route('/reservas/eliminar/<int:id_reserva>', methods=['POST'])
def eliminar_reserva(id_reserva):
    session = DBSession()
    try:
        reserva = session.query(Reservas).filter_by(id_reserva=id_reserva).one()
        session.delete(reserva)
        session.commit()
        flash('Reserva eliminada correctamente', 'success')
    except Exception as e:
        session.rollback()
        flash(f'Error al eliminar reserva: {e}', 'error')
    session.close()
    return redirect(url_for('listar_reservas'))


if __name__ == '__main__':
    app.run(debug=True)
