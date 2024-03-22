document.addEventListener("DOMContentLoaded", function () {
    const themeToggleBtn = document.getElementById("theme-toggle");
    themeToggleBtn.addEventListener("click", () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        document.documentElement.setAttribute("data-theme", currentTheme === "dark" ? "" : "dark");
        localStorage.setItem("theme", currentTheme === "dark" ? "" : "dark")
    });
});