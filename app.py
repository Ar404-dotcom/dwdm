import os
from flask import Flask, request
from PIL import Image

app = Flask(__name__)

# Get the absolute path to the 'static' directory
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# Ensure the static directory exists
if not os.path.exists(static_dir):
    os.makedirs(static_dir)
    print(f"Created 'static' directory at: {static_dir}")  # Debug statement

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the file is present
        if 'file' not in request.files:
            return "No file part in the request", 400
        
        file = request.files['file']
        
        # Check if the file is selected
        if file.filename == '':
            return "No selected file", 400
        
        # Check if the file is an image
        if file and file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            try:
                new_width = int(request.form.get('width', 0))
                new_height = int(request.form.get('height', 0))
                
                if new_width <= 0 or new_height <= 0:
                    return "Width and height must be positive integers", 400
                
                img = Image.open(file)
                resized_img = img.resize((new_width, new_height))
                
                # Use absolute path for saving the image
                output_path = os.path.join(static_dir, 'output.jpg')
                resized_img.save(output_path, quality=95)  # Save with high quality
                
                return f"<img src='static/output.jpg' alt='Resized Image'>"
            
            except Exception as e:
                return f"An error occurred: {str(e)}", 500
        else:
            return "Invalid file type. Please upload an image.", 400
    
    return '''
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <input type="number" name="width" placeholder="Width" required>
        <input type="number" name="height" placeholder="Height" required>
        <input type="submit" value="Resize">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)