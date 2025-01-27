// Check if a theme is stored in localStorage
const storedTheme = localStorage.getItem('theme');
const themeStylesheet = document.getElementById('theme-stylesheet');

if (storedTheme === 'dark') {
    themeStylesheet.href = "/static/themes/dark.css";
} else {
    themeStylesheet.href = "/static/themes/light.css";
}

// Function to toggle theme
function toggleTheme() {
    const currentTheme = themeStylesheet.getAttribute('href');

    if (currentTheme.includes('light.css')) {
        themeStylesheet.href = "/static/themes/dark.css";
        localStorage.setItem('theme', 'dark');
    } else {
        themeStylesheet.href = "/static/themes/light.css";
        localStorage.setItem('theme', 'light');
    }
}

// Export the toggleTheme function if needed elsewhere
export { toggleTheme };
