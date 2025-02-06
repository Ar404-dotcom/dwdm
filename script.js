document.getElementById('uploadForm').addEventListener('submit', function(event) {
    const fileInput = document.getElementById('fileInput');
    const width = document.getElementById('width').value;
    const height = document.getElementById('height').value;

    if (!fileInput.files.length) {
        alert("Please select an image file.");
        event.preventDefault();
    } else if (width <= 0 || height <= 0) {
        alert("Width and height must be greater than zero.");
        event.preventDefault();
    }
});
