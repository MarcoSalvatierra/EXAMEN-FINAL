CREATE TABLE Aeropuertos (
    codigo_aeropuerto VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(100),
    pais VARCHAR(100)
);

CREATE TABLE Vuelos (
    numero_vuelo VARCHAR(10) PRIMARY KEY,
    origen VARCHAR(10) REFERENCES Aeropuertos(codigo_aeropuerto),
    destino VARCHAR(10) REFERENCES Aeropuertos(codigo_aeropuerto),
    fecha DATE,
    hora_salida TIME,
    hora_llegada TIME,
    estado VARCHAR(50) -- ej. 'Programado', 'Cancelado', 'Retrasado'
);

select * from vuelos;

CREATE TABLE Pasajeros (
    id_pasajero SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    email VARCHAR(100),
    telefono VARCHAR(20)
);

CREATE TABLE Asientos (
    id_asiento SERIAL PRIMARY KEY,
    numero_vuelo VARCHAR(10) REFERENCES Vuelos(numero_vuelo),
    numero_asiento VARCHAR(5),
    clase VARCHAR(50), -- ej. 'Economica', 'Primera'
    disponible BOOLEAN DEFAULT TRUE
);

CREATE TABLE Reservas (
    id_reserva SERIAL PRIMARY KEY,
    id_pasajero INT REFERENCES Pasajeros(id_pasajero),
    id_asiento INT REFERENCES Asientos(id_asiento),
    fecha_reserva DATE,
    estado VARCHAR(50) -- ej. 'Confirmada', 'Cancelada'
);

INSERT INTO Aeropuertos (codigo_aeropuerto, nombre, ciudad, pais) VALUES
('JFK', 'John F. Kennedy International Airport', 'New York', 'USA'),
('LAX', 'Los Angeles International Airport', 'Los Angeles', 'USA'),
('LHR', 'Heathrow Airport', 'London', 'UK'),
('CDG', 'Charles de Gaulle Airport', 'Paris', 'France'),
('NRT', 'Narita International Airport', 'Tokyo', 'Japan');

INSERT INTO Vuelos (numero_vuelo, origen, destino, fecha, hora_salida, hora_llegada, estado) VALUES
('AA100', 'JFK', 'LAX', '2024-07-01', '08:00', '11:00', 'Programado'),
('BA200', 'LHR', 'CDG', '2024-07-02', '09:00', '10:30', 'Programado'),
('JL300', 'NRT', 'JFK', '2024-07-03', '12:00', '06:00', 'Programado'),
('AF400', 'CDG', 'NRT', '2024-07-04', '14:00', '09:00', 'Programado'),
('DL500', 'LAX', 'LHR', '2024-07-05', '16:00', '10:00', 'Programado');

INSERT INTO Pasajeros (nombre, apellido, email, telefono) VALUES
('John', 'Doe', 'john.doe@example.com', '1234567890'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321'),
('Michael', 'Johnson', 'michael.johnson@example.com', '5556667777'),
('Emily', 'Davis', 'emily.davis@example.com', '4445556666'),
('David', 'Brown', 'david.brown@example.com', '3334445555');

INSERT INTO Asientos (numero_vuelo, numero_asiento, clase, disponible) VALUES
('AA100', '1A', 'Primera', TRUE),
('AA100', '1B', 'Primera', TRUE),
('AA100', '10C', 'Economica', TRUE),
('BA200', '2A', 'Primera', TRUE),
('BA200', '2B', 'Primera', TRUE),
('BA200', '20C', 'Economica', TRUE),
('JL300', '3A', 'Primera', TRUE),
('JL300', '3B', 'Primera', TRUE),
('JL300', '30C', 'Economica', TRUE),
('AF400', '4A', 'Primera', TRUE),
('AF400', '4B', 'Primera', TRUE),
('AF400', '40C', 'Economica', TRUE),
('DL500', '5A', 'Primera', TRUE),
('DL500', '5B', 'Primera', TRUE),
('DL500', '50C', 'Economica', TRUE);

INSERT INTO Reservas (id_pasajero, id_asiento, fecha_reserva, estado) VALUES
(1, 1, '2024-06-01', 'Confirmada'),
(2, 2, '2024-06-02', 'Confirmada'),
(3, 3, '2024-06-03', 'Confirmada'),
(4, 4, '2024-06-04', 'Confirmada'),
(5, 5, '2024-06-05', 'Confirmada');
