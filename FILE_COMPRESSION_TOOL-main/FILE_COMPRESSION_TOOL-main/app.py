from flask import Flask, render_template, request, send_file, jsonify
import os
from huffman import compress, decompress
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
COMPRESSED_FOLDER = 'compressed'
DECOMPRESSED_FOLDER = 'decompressed'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COMPRESSED_FOLDER, exist_ok=True)
os.makedirs(DECOMPRESSED_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'txt', 'log', 'csv', 'json', 'xml', 'html', 'css', 'js', 'py', 'java', 'cpp', 'c', 'md'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_size(filepath):
    return os.path.getsize(filepath)

def calculate_compression_ratio(original_size, compressed_size):
    if original_size == 0:
        return 0
    return ((original_size - compressed_size) / original_size) * 100

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/compress')
def compress_page():
    return render_template('compress.html')

@app.route('/decompress')
def decompress_page():
    return render_template('decompress.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/compress', methods=['POST'])
def compress_route():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Only text-based files are allowed.'}), 400
        
        filename = secure_filename(file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        output_filename = filename.rsplit('.', 1)[0] + '.huff'
        output_path = os.path.join(COMPRESSED_FOLDER, output_filename)
        
        file.save(input_path)
        
        original_size = get_file_size(input_path)
        compress(input_path, output_path)
        compressed_size = get_file_size(output_path)
        
        compression_ratio = calculate_compression_ratio(original_size, compressed_size)
        
        # Clean up original file
        os.remove(input_path)
        
        return send_file(
            output_path, 
            as_attachment=True,
            download_name=output_filename,
            mimetype='application/octet-stream'
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/decompress', methods=['POST'])
def decompress_route():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        filename = secure_filename(file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        
        # Remove .huff extension and add .txt
        base_name = filename.rsplit('.', 1)[0] if '.' in filename else filename
        output_filename = base_name + '_decompressed.txt'
        output_path = os.path.join(DECOMPRESSED_FOLDER, output_filename)
        
        file.save(input_path)
        
        decompress(input_path, output_path)
        
        # Clean up compressed file
        os.remove(input_path)
        
        return send_file(
            output_path, 
            as_attachment=True,
            download_name=output_filename,
            mimetype='text/plain'
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)