// Función que crea el HTML para un producto usando template literals
function CrearProductoHTML(producto) {
  return `
    <div class="col-md-4 mb-4">
      <div class="card">
        <img src="${producto.imagen}" class="card-img-top" alt="${producto.nombre}" />
        <div class="card-body">
          <h5 class="card-title">${producto.nombre}</h5>
          <p class="card-text">${producto.descripcion}</p>
          <p><strong>$${producto.precio.toFixed(2)}</strong></p>
        </div>
      </div>
    </div>
  `;
}

// Función para cargar los productos desde la API según la categoría
async function cargarProductos(categoria) {
  // Obtener el contenedor correspondiente a la categoría
  const contenedor = document.getElementById(`productos-${categoria}`);

  if (!contenedor) {
    console.error(`No existe el contenedor para la categoría: ${categoria}`);
    return;
  }

  // Mostrar un mensaje mientras carga
  contenedor.innerHTML = "Cargando...";

  try {
    // Llamar a la API con fetch
    const response = await fetch(`/api/products/${categoria}`);

    if (!response.ok) {
      throw new Error("Error al cargar los productos");
    }

    // Convertir la respuesta en JSON (lista)
    const productos = await response.json();

    // Si no hay productos, mostrar mensaje
    if (productos.length === 0) {
      contenedor.innerHTML = '<p>No hay productos disponibles en esta categoría.</p>';
      return;
    }

    // Crear el HTML de todos los productos usando map
    const htmlProductos = productos.map(CrearProductoHTML).join('');

    // Insertar el html en el contenedor
    contenedor.innerHTML = htmlProductos;

  } catch (error) {
    // Mostrar mensaje en el contenedor en caso de error
    contenedor.innerHTML = `<p>Error: ${error.message}</p>`;
  }
}

// Ejecuta cuando el documento está completamente cargado
document.addEventListener('DOMContentLoaded', () => {
  // Al cargar la página, mostramos los productos de la categoría por defecto (camisas)
  cargarProductos('camisas');

  // Seleccionamos todos los botones de pestañas que cambian la categoría
  const tabs = document.querySelectorAll('#tabs button[data-bs-toggle="tab"]');

  // A cada pestaña le agregamos un evento para detectar cuándo se activa
  tabs.forEach(tab => {
    tab.addEventListener('shown.bs.tab', (event) => {
      // Obtenemos el nombre de la categoría desde el atributo data-bs-target
      const categoria = event.target.getAttribute('data-bs-target').substring(1); // Eliminamos el #

      // Cargamos los productos de la nueva categoría seleccionada
      cargarProductos(categoria);
    });
  });
});
