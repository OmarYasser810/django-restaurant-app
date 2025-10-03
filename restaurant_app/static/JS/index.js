document.addEventListener("DOMContentLoaded", function() {
    // Select the icon by its class
    const nightIcon = document.querySelector('.fa-circle-half-stroke');
    if (nightIcon) {
        nightIcon.style.cursor = "pointer";
        nightIcon.title = "Toggle Night Mode";
        nightIcon.addEventListener("click", function() {
            document.body.classList.toggle("night-mode");
        });
    }
});