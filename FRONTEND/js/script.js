const menuBtn = document.getElementById("menuBtn");
const navlinks = document.getElementById("navlinks");
const links = navlinks.querySelectorAll("a");

// 1. Control del botón hamburguesa (Abrir / Cerrar)
menuBtn.addEventListener("click", () => {
    navlinks.classList.toggle("active");
    
    if (navlinks.classList.contains("active")) {
        menuBtn.innerHTML = "✕"; // Tip de Senior: Usar '✕' (simbolo de cierre) se ve más simétrico que la 'x' del teclado
        menuBtn.setAttribute("aria-expanded", "true");
    } else {
        menuBtn.innerHTML = "☰";
        menuBtn.setAttribute("aria-expanded", "false");
    }
});

// 2. Cerrar el menú cuando se hace click en un enlace interno
links.forEach(link => {
    link.addEventListener("click", () => {
        navlinks.classList.remove("active");
        menuBtn.innerHTML = "☰";
        menuBtn.setAttribute("aria-expanded", "false");
    });
});

// 3. NUEVO: Cerrar el menú automáticamente al hacer click afuera de él
document.addEventListener("click", (event) => {
    // Si el menú está abierto Y el click NO fue dentro de los enlaces Y tampoco en el botón...
    if (navlinks.classList.contains("active") && !navlinks.contains(event.target) && !menuBtn.contains(event.target)) {
        navlinks.classList.remove("active");
        menuBtn.innerHTML = "☰";
        menuBtn.setAttribute("aria-expanded", "false");
    }
});