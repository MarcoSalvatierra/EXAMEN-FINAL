from sqlalchemy import Column, Integer, String, Boolean, Date, Time, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Aeropuertos(Base):
    __tablename__ = 'aeropuertos'
    
    codigo_aeropuerto = Column(String(10), primary_key=True)
    nombre = Column(String(100))
    ciudad = Column(String(100))
    pais = Column(String(100))

class Vuelos(Base):
    __tablename__ = 'vuelos'
    
    numero_vuelo = Column(String(10), primary_key=True)
    origen = Column(String(10), ForeignKey('aeropuertos.codigo_aeropuerto'))
    destino = Column(String(10), ForeignKey('aeropuertos.codigo_aeropuerto'))
    fecha = Column(Date)
    hora_salida = Column(Time)
    hora_llegada = Column(Time)
    estado = Column(String(50))

    # Relaciones
    aeropuerto_origen = relationship('Aeropuertos', foreign_keys=[origen])
    aeropuerto_destino = relationship('Aeropuertos', foreign_keys=[destino])

class Pasajeros(Base):
    __tablename__ = 'pasajeros'
    
    id_pasajero = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    apellido = Column(String(100))
    email = Column(String(100))
    telefono = Column(String(20))

class Asientos(Base):
    __tablename__ = 'asientos'
    
    id_asiento = Column(Integer, primary_key=True, autoincrement=True)
    numero_vuelo = Column(String(10), ForeignKey('vuelos.numero_vuelo'))
    numero_asiento = Column(String(5))
    clase = Column(String(50))
    disponible = Column(Boolean, default=True)

    # Relaciones
    vuelo = relationship('Vuelos')

class Reservas(Base):
    __tablename__ = 'reservas'
    
    id_reserva = Column(Integer, primary_key=True, autoincrement=True)
    id_pasajero = Column(Integer, ForeignKey('pasajeros.id_pasajero'))
    id_asiento = Column(Integer, ForeignKey('asientos.id_asiento'))
    fecha_reserva = Column(Date)
    estado = Column(String(50))

    # Relaciones
    pasajero = relationship('Pasajeros')
    asiento = relationship('Asientos')


