document.addEventListener('DOMContentLoaded', function() {
    // Código que se ejecuta cuando el DOM ha sido completamente cargado

    // Ejemplo de validación de formulario utilizando JavaScript
    const formularioAgregarAeropuerto = document.querySelector('form');
    if (formularioAgregarAeropuerto) {
        formularioAgregarAeropuerto.addEventListener('submit', function(event) {
            event.preventDefault(); // Previene el envío por defecto del formulario

            // Validación de campos (puedes agregar más validaciones según tus requisitos)
            const codigoAeropuerto = document.getElementById('codigo_aeropuerto').value.trim();
            const nombre = document.getElementById('nombre').value.trim();
            const ciudad = document.getElementById('ciudad').value.trim();
            const pais = document.getElementById('pais').value.trim();

            if (codigoAeropuerto === '' || nombre === '' || ciudad === '' || pais === '') {
                alert('Por favor, complete todos los campos.');
                return;
            }

            // Envío de datos mediante fetch (puedes usar AJAX si prefieres)
            const formData = new FormData();
            formData.append('codigo_aeropuerto', codigoAeropuerto);
            formData.append('nombre', nombre);
            formData.append('ciudad', ciudad);
            formData.append('pais', pais);

            fetch('/aeropuertos/agregar', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Manejar la respuesta del servidor (puedes mostrar un mensaje de éxito, por ejemplo)
                console.log('Respuesta del servidor:', data);
                alert('Aeropuerto agregado correctamente.');
                // Opcional: Redirigir a otra página después de agregar el aeropuerto
                window.location.href = '/aeropuertos'; // Redirige a la lista de aeropuertos
            })
            .catch(error => {
                console.error('Error al agregar aeropuerto:', error);
                alert('Hubo un error al agregar el aeropuerto. Por favor, inténtelo nuevamente.');
            });
        });
    }
});
