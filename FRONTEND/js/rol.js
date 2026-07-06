document.addEventListener("DOMContentLoaded", () => {

    const botones = document.querySelectorAll(".role-btn");

    botones.forEach(btn => {

        btn.addEventListener("click", () => {

            const rol = btn.dataset.rol;

            localStorage.setItem("rol", rol);

            window.location.href = "dashboard.html";

        });

    });

});

document.querySelector(".comprador").addEventListener("click", () => {
    localStorage.setItem("rol", "comprador");
    window.location.href = "dashboard.html";
});

document.querySelector(".vendedor").addEventListener("click", () => {
    localStorage.setItem("rol", "vendedor");
    window.location.href = "dashboard.html";
});

document.querySelector(".ambos").addEventListener("click", () => {
    localStorage.setItem("rol", "ambos");
    window.location.href = "dashboard.html";
});