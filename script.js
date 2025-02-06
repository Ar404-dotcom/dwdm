// static/js/script.js
document.addEventListener('DOMContentLoaded', function () {
    console.log('JavaScript is working!');

    // Example: Add an alert when the form is submitted
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        alert('Form submitted!');
    });
});
