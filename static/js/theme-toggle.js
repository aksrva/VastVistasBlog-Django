document.addEventListener("DOMContentLoaded", function () {
    const themeToggleBtn = document.getElementById("theme-toggle");
    document.body.dataset.theme = localStorage.getItem("theme");
    themeToggleBtn.addEventListener("click", () => {
        document.body.dataset.theme = localStorage.getItem("theme") === "dark" ? "" : "dark";
        localStorage.setItem("theme", document.body.dataset.theme)
    });
});