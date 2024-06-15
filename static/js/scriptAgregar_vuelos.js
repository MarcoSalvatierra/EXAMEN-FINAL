document.addEventListener('DOMContentLoaded', function() {
    // Código que se ejecuta cuando el DOM ha sido completamente cargado

    // Ejemplo de validación de formulario utilizando JavaScript
    const formularioAgregarVuelo = document.querySelector('form');
    if (formularioAgregarVuelo) {
        formularioAgregarVuelo.addEventListener('submit', function(event) {
            event.preventDefault(); // Previene el envío por defecto del formulario

            // Validación de campos (puedes agregar más validaciones según tus requisitos)
            const numeroVuelo = document.getElementById('numero_vuelo').value.trim();
            const origen = document.getElementById('origen').value;
            const destino = document.getElementById('destino').value;
            const fecha = document.getElementById('fecha').value;
            const horaSalida = document.getElementById('hora_salida').value;
            const horaLlegada = document.getElementById('hora_llegada').value;
            const estado = document.getElementById('estado').value.trim();

            if (numeroVuelo === '' || origen === '' || destino === '' || fecha === '' || horaSalida === '' || horaLlegada === '' || estado === '') {
                alert('Por favor, complete todos los campos.');
                return;
            }

            // Envío de datos mediante fetch (puedes usar AJAX si prefieres)
            const formData = new FormData();
            formData.append('numero_vuelo', numeroVuelo);
            formData.append('origen', origen);
            formData.append('destino', destino);
            formData.append('fecha', fecha);
            formData.append('hora_salida', horaSalida);
            formData.append('hora_llegada', horaLlegada);
            formData.append('estado', estado);

            fetch('/vuelos/agregar', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Manejar la respuesta del servidor (puedes mostrar un mensaje de éxito, por ejemplo)
                console.log('Respuesta del servidor:', data);
                alert('Vuelo agregado correctamente.');
                // Opcional: Redirigir a otra página después de agregar el vuelo
                window.location.href = '/vuelos'; // Redirige a la lista de vuelos
            })
            .catch(error => {
                console.error('Error al agregar vuelo:', error);
                alert('Hubo un error al agregar el vuelo. Por favor, inténtelo nuevamente.');
            });
        });
    }
});
