🗜️ File Compression Tool
A modern web-based file compression tool using Huffman Coding algorithm. This application provides lossless compression for text-based files with an intuitive and beautiful user interface.

Python Flask License

✨ Features
Lossless Compression: Original data is perfectly preserved
Huffman Coding Algorithm: Efficient variable-length encoding
Modern UI: Beautiful, responsive design with drag-and-drop support
Multiple File Types: Supports TXT, LOG, CSV, JSON, XML, HTML, CSS, JS, Python, Java, C, C++, Markdown
Fast Processing: Quick compression and decompression
Secure: Files are processed locally and not stored permanently
Real-time Feedback: Progress indicators and error handling
🎯 How It Works
Huffman Coding Algorithm
Huffman coding is a lossless data compression algorithm that:

Analyzes character frequency in the input text
Builds a binary tree where frequent characters have shorter codes
Generates unique binary codes for each character
Encodes the text using these variable-length codes
Saves space by using fewer bits for common characters
Example
Original text: "AAABBC"
Character frequencies: A=3, B=2, C=1

Huffman codes might be:
A -> 0
B -> 10
C -> 11

Encoded: "000101011" (9 bits vs 48 bits in ASCII)
Compression ratio: ~81% reduction
🚀 Getting Started
Prerequisites
Python 3.7 or higher
pip (Python package manager)
Installation
Clone the repository

git clone https://github.com/yourusername/file-compression-tool.git
cd file-compression-tool
Create a virtual environment (recommended)

python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
Install dependencies

pip install flask
Run the application

python app.py
Open in browser

http://localhost:5000
📁 Project Structure
file-compression-tool/
│
├── app.py                 # Flask application and routes
├── huffman.py            # Huffman coding implementation
├── README.md             # Project documentation
│
├── templates/            # HTML templates
│   ├── home.html        # Landing page
│   ├── compress.html    # Compression page
│   └── decompress.html  # Decompression page
│
├── uploads/             # Temporary upload storage (created automatically)
├── compressed/          # Compressed files storage (created automatically)
└── decompressed/        # Decompressed files storage (created automatically)
💻 Usage
Compressing Files
Navigate to the Compress page
Click the upload area or drag and drop a text file
Supported formats: .txt, .log, .csv, .json, .xml, .html, .css, .js, .py, .java, .cpp, .c, .md
Click Compress File
Download the .huff compressed file
Decompressing Files
Navigate to the Decompress page
Upload a .huff file (previously compressed by this tool)
Click Decompress File
Download the restored original text file
🎨 UI Features
Gradient Backgrounds: Eye-catching color schemes
Drag & Drop: Easy file upload
Progress Indicators: Visual feedback during processing
Responsive Design: Works on desktop, tablet, and mobile
Smooth Animations: Professional transitions and effects
Error Handling: Clear error messages and validation
🔧 API Endpoints
GET /
Home page with navigation

GET /compress
Compression interface

POST /compress
Input: Multipart form data with file
Output: Compressed .huff file download
Errors: 400 (invalid file), 500 (processing error)
GET /decompress
Decompression interface

POST /decompress
Input: Multipart form data with .huff file
Output: Decompressed .txt file download
Errors: 400 (invalid file), 500 (processing error)
📊 Performance
Compression Ratios (Typical)
File Type	Average Compression
Plain Text	40-60%
Source Code	50-70%
JSON	60-80%
Logs	50-70%
Note: Actual compression depends on character frequency distribution

Limitations
Best suited for text-based files
Small files (< 100 bytes) may not compress well
Binary files are not supported
Very random data compresses poorly
🛠️ Technical Details
Algorithm Complexity
Time Complexity: O(n log n) for building tree, O(n) for encoding
Space Complexity: O(n) for tree storage
File Format
Compressed .huff files contain:

Padding information (1 byte)
Pickled Huffman code dictionary
Compressed binary data
🔐 Security
Files are processed server-side temporarily
Original uploads are deleted after processing
No permanent storage of user files
No tracking or analytics
🐛 Troubleshooting
Common Issues
Error: "Cannot compress empty file"

Ensure the file contains text data
Error: "Invalid file type"

Check that file extension is in the supported list
Decompression fails

Ensure the file was compressed by this tool
File may be corrupted
Port already in use

# Change port in app.py
app.run(debug=True, port=5001)
🚧 Future Enhancements
 Support for additional compression algorithms (LZW, LZ77)
 Batch file processing
 Compression statistics and analytics
 File comparison tool
 Cloud storage integration
 Password protection for compressed files
 Command-line interface (CLI)
🤝 Contributing
Contributions are welcome! Here's how:

Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
📝 License
This project is licensed under the MIT License - see below for details:

MIT License

Copyright (c) 2025 [Sagar Sarkar]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
👨‍💻 Author
Sagar Sarkar


Email: sagarsarkar2424@gmail.com
🙏 Acknowledgments
Huffman Coding algorithm by David A. Huffman (1952)
Flask web framework
Google Fonts (Inter font family)
Community contributors
📚 Resources
Huffman Coding - Wikipedia
Flask Documentation
Data Compression Algorithms
📞 Support
For issues, questions, or suggestions:

Email: sagarsarkar2424@gmail.com
⭐ Star this repository if you find it helpful!

Made with ❤️ and Python
