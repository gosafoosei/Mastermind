/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html'],
  theme: {
    extend: {
      fontFamily: {
        code: ['"Fira Code"', 'monospace'],
        stencil: ['"Saira Stencil One"', 'sans-serif'],
        sans: ['Inter', 'sans-serif'],
      },
      colors: {
        silver: {
          100: '#f3f4f6',
          300: '#d1d5db',
          500: '#9ca3af',
          700: '#4b5563',
          900: '#1f2937',
        },
      },
    },
  },
};
