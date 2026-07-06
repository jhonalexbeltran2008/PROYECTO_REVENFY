document.addEventListener("DOMContentLoaded", () => {
    const hamburger = document.getElementById("hamburger");
const navMenu = document.getElementById("navMenu");

hamburger.addEventListener("click", () => {
    navMenu.classList.toggle("active");
});
    const btn = document.querySelector(".dash-menu-hamburger");
    const sidebar = document.getElementById("dashSidebar");
    const overlay = document.getElementById("sidebarOverlay");

    if (!btn || !sidebar || !overlay) return;

    function openMenu() {
        sidebar.classList.add("open");
        overlay.classList.add("visible");
    }

    function closeMenu() {
        sidebar.classList.remove("open");
        overlay.classList.remove("visible");
    }

    function toggleMenu() {
        if (window.innerWidth <= 768) {
            sidebar.classList.toggle("open");
            overlay.classList.toggle("visible");
        }
    }

    btn.addEventListener("click", toggleMenu);
    overlay.addEventListener("click", closeMenu);

    // 🔥 FIX CLAVE: evita que quede abierto en resize
    window.addEventListener("resize", () => {
        if (window.innerWidth > 768) {
            closeMenu();
        }
    });

    // 🔥 FIX CLAVE: estado inicial limpio
    closeMenu();

}); 