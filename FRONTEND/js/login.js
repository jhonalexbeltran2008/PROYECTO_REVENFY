
// 1. CONTROL DE VISIBILIDAD DE CONTRASEÑA

const togglePasswordBtn = document.getElementById("togglePassword");
const passwordInput = document.getElementById("password");

togglePasswordBtn.addEventListener("click", function() {
    // Buscamos el ícono de FontAwesome dentro del botón
    const icon = this.querySelector("i");
    
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        icon.classList.remove("fa-eye");
        icon.classList.add("fa-eye-slash");
    } else {
        passwordInput.type = "password";
        icon.classList.remove("fa-eye-slash");
        icon.classList.add("fa-eye");
    }
});



// 2. AUTENTICACIÓN CON LOCALSTORAGE

document.getElementById("loginForm").addEventListener("submit", function(e) {
    e.preventDefault();

    let correo = document.getElementById("correo").value;
    let password = passwordInput.value; // Reutilizamos la referencia de arriba

    // Traemos el objeto del usuario registrado en el LocalStorage
    let usuarioGuardado = JSON.parse(localStorage.getItem("usuario"));

    // Validación de credenciales
    if (
        usuarioGuardado &&
        correo === usuarioGuardado.correo &&
        password === usuarioGuardado.password
    ) {
        // Creamos la sesión en el navegador
        localStorage.setItem("sesion", "activa");
        
        // Redirección al Dashboard de Revenfy
        window.location.href = "rol.html";
    } else {
        // Alerta en caso de error
        alert("Correo o contraseña incorrectos");
    }
});