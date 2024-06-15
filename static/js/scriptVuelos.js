document.addEventListener('DOMContentLoaded', function() {
    // Código que se ejecuta cuando el DOM ha sido completamente cargado

    // Ejemplo de manejo de eventos de clic en un enlace o botón
    const agregarVueloBtn = document.querySelector('.btn');
    if (agregarVueloBtn) {
        agregarVueloBtn.addEventListener('click', function(event) {
            // Redirecciona al usuario a la página de agregar vuelo
            window.location.href = '/vuelos/agregar';
        });
    }

    // Ejemplo de filtrado de datos (puedes adaptar según tus necesidades)
    const filtroEstado = document.getElementById('filtroEstado');
    if (filtroEstado) {
        filtroEstado.addEventListener('change', function(event) {
            const estadoSeleccionado = event.target.value;
            // Aquí podrías hacer una petición AJAX para obtener vuelos filtrados por estado
            console.log('Estado seleccionado:', estadoSeleccionado);
            // Por ejemplo, puedes actualizar la lista de vuelos en la página
            // Considera cómo deseas mostrar y manipular los datos en vuelos.html
        });
    }
});
