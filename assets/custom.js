// Espera a que todo el contenido del DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {

  // Función principal que activa visualmente la sección más cercana al centro de la pantalla
  function activateSection() {
    // Selecciona todas las secciones con la clase .scroll-section
    const sections = document.querySelectorAll('.scroll-section');

    // Si no hay secciones aún (por ejemplo, la página no terminó de cargar), salir
    if (!sections.length) return;

    let closestSection = null; // Sección más cercana al centro de la pantalla
    let closestDistance = Number.POSITIVE_INFINITY; // Inicializa con distancia infinita
    const viewportCenter = window.innerHeight / 2; // Calcula el centro vertical de la pantalla

    // Itera por todas las secciones
    sections.forEach(section => {
      const rect = section.getBoundingClientRect(); // Obtiene la posición y tamaño relativo al viewport
      const sectionCenter = rect.top + rect.height / 2; // Centro vertical de la sección
      const distance = Math.abs(sectionCenter - viewportCenter); // Distancia entre centro de sección y del viewport

      // Guarda la sección más cercana al centro
      if (distance < closestDistance) {
        closestDistance = distance;
        closestSection = section;
      }
    });

    // Quita la clase 'active' de todas las secciones
    sections.forEach(section => {
      section.classList.remove('active');
    });

    // Añade la clase 'active' solo a la sección más cercana al centro
    if (closestSection) {
      closestSection.classList.add('active');
    }
  }

  // Ejecutar activateSection cada vez que el usuario hace scroll
  window.addEventListener('scroll', activateSection);

  // También se vuelve a ejecutar si se redimensiona la ventana
  window.addEventListener('resize', activateSection);

  // Se ejecuta una vez después de 500ms para asegurarse de aplicar el efecto tras la carga
  setTimeout(activateSection, 500);
});
