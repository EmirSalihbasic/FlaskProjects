from flask import Flask, render_template, request

app = Flask(__name__)

# Set the upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file was submitted with the request
    if 'file' not in request.files:
        return 'No file part in the request'
    
    file = request.files['file']
    
    # Check if the file is empty
    if file.filename == '':
        return 'No selected file'
    
    # Check if the file extension is allowed
    if not allowed_file(file.filename):
        return 'File type not allowed'
    
    # Save the file to the upload folder
    file.save(f"uploads/{file.filename}")
    
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run()
