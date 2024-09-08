/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./institute/templates/**/*.{html,js}', './institute/templates/**/**/*.{html,js}'],
    theme: {
        extend: {
            fontFamily: {
                robotoSans: ['Roboto', 'sans-serif'],
                robotoCondensed: ['Roboto Condensed', 'sans-serif'],
                sans: ['Open Sans', 'sans-serif'],
            },
            fontWeight: {
                extraBold: '1000',
            },
            colors: {
                primary: '#0080ff',
            },
        },
    },
    plugins: [],
};
