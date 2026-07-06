document.addEventListener("DOMContentLoaded", () => {
    const registroForm = document.getElementById("registroForm");
    const toggleButtons = document.querySelectorAll(".toggle-password");

    // ==========================================
    // 1. MANEJO INTERACTIVO DE LOS OJOS (INPUTS)
    // ==========================================
    toggleButtons.forEach(button => {
        button.addEventListener("click", function() {
            // Obtenemos el ID del input desde el atributo data-target
            const targetId = this.getAttribute("data-target");
            const inputField = document.getElementById(targetId);
            const icon = this.querySelector("i");

            if (inputField.type === "password") {
                inputField.type = "text";
                icon.classList.remove("bi-eye");
                icon.classList.add("bi-eye-slash");
            } else {
                inputField.type = "password";
                icon.classList.remove("bi-eye-slash");
                icon.classList.add("bi-eye");
            }
        });
    });

    // ==========================================
    // 2. PROCESAMIENTO DEL REGISTRO
    // ==========================================
    registroForm.addEventListener("submit", function(e) {
        e.preventDefault();

        const nombre = document.getElementById("nombre").value.trim();
        const correo = document.getElementById("correo").value.trim();
        const password = document.getElementById("password").value;
        const confirmar = document.getElementById("confirmarPassword").value;

        // Validación: Campos vacíos por espacios
        if (!nombre || !correo) {
            alert("Por favor rellena todos los campos de forma válida.");
            return;
        }

        // Validación: Contraseñas idénticas
        if (password !== confirmar) {
            alert("Las contraseñas no coinciden");
            return;
        }

        // Estructura del payload
        const usuario = {
            nombre,
            correo,
            password
        };

        // Guardado local persistente
        localStorage.setItem("usuario", JSON.stringify(usuario));

        alert("¡Registro exitoso! Ya puedes iniciar sesión.");
        window.location.href = "login.html";
    });
});