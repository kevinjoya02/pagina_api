// Función que crea el HTML para un producto usando template literals
function CrearProductoHTML(producto) {
  return `
    <div class="col-md-4 mb-4">
      <div class="card">
        <img 
          src="${producto.imagen}" 
          class="card-img-top"  
          style="width: 100%; height: 200px; object-fit: contain;" 
        />
        <div class="card-body">
          <h5 class="card-title">${producto.nombre}</h5>
          <p class="card-text">${producto.descripcion}</p>
          <p><strong>$${producto.precio.toFixed(2)}</strong></p>
          <button 
            class="btn btn-primary comprar-btn" 
            data-nombre="${producto.nombre}" 
            data-id="${producto.id}">
            comprar
          </button>
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
    const response = await fetch(`/api/productos/${categoria}`);

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

const botonesComprar = contenedor.querySelectorAll(".comprar-btn");
botonesComprar.forEach(boton => {
  boton.addEventListener("click", async () => {
    const nombreProducto = boton.getAttribute("data-nombre");
    
    //obtener fecha de entrega desde la API
    let fechaEntrega = "proximamente";
    try 
    {
      const response = await fetch("/api/fecha_entrega");
      const data = await response.json();
      fechaEntrega = data.fecha_entrega;

    } 
    catch (error) 
    {
      console.error("Error al obtener fecha de entrega:", error);
    }

    // Cambiamos el texto del modal dinámicamente
    const mensajeCompra = document.getElementById("mensajeCompra");
    mensajeCompra.textContent = `Tu producto "${nombreProducto}" será entregado el ${fechaEntrega} 🚚`;

    // Mostramos el modal con Bootstrap
    const modalCompraEl = document.getElementById("modalCompra");
    const modal = new bootstrap.Modal(modalCompraEl);
    modal.show();

    // Agregamos el evento al botón "Aceptar"
    const btnAceptar = document.getElementById("btnAceptarCompra");
btnAceptar.onclick = async () => {
  modal.hide(); // Cierra el modal

  // Eliminamos visualmente la tarjeta del producto
  const card = boton.closest(".col-md-4");
  if (card) card.remove();

  // Eliminamos del backend (temporal en memoria)
  const productoId = boton.getAttribute("data-id");
  const categoria = contenedor.id.replace('productos-', '');
  await fetch(`/api/productos/${categoria}/${productoId}`, { method: "DELETE" });

  alert(`✅ Has comprado "${nombreProducto}".`);
};
  });
});

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
