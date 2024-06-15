document.addEventListener('DOMContentLoaded', function() {
    // Código que se ejecuta cuando el DOM ha sido completamente cargado

    // Ejemplo de manejo de un evento de clic en un botón
    const agregarAeropuertoBtn = document.querySelector('#agregarAeropuertoBtn');
    if (agregarAeropuertoBtn) {
        agregarAeropuertoBtn.addEventListener('click', function(event) {
            event.preventDefault(); // Previene el comportamiento por defecto del enlace o botón
            // Redirecciona al usuario a la página de agregar aeropuerto
            window.location.href = '/aeropuertos/agregar';
        });
    }

    // Ejemplo de peticion AJAX para cargar datos adicionales
    const cargarDatosBtn = document.querySelector('#cargarDatosBtn');
    if (cargarDatosBtn) {
        cargarDatosBtn.addEventListener('click', function(event) {
            event.preventDefault();
            // Puedes usar fetch u otra librería AJAX (como axios) para hacer la petición
            fetch('/ruta_para_cargar_datos')
                .then(response => response.json())
                .then(data => {
                    // Manipular los datos recibidos
                    console.log('Datos recibidos:', data);
                    // Por ejemplo, actualizar la tabla de aeropuertos con los nuevos datos
                    // Aquí deberías tener tu lógica específica para actualizar la interfaz
                })
                .catch(error => {
                    console.error('Error al cargar datos:', error);
                });
        });
    }
});
