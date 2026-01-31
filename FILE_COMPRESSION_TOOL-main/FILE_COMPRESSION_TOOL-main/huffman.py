import heapq
import pickle
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_tree(text):
    """Build Huffman tree from text"""
    if not text:
        raise ValueError("Cannot compress empty file")
    
    frequency = Counter(text)
    
    # Handle single character case
    if len(frequency) == 1:
        char = list(frequency.keys())[0]
        root = Node(char, frequency[char])
        return root
    
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes(root):
    """Generate Huffman codes from tree"""
    if root.char is not None:
        # Single character case
        return {root.char: '0'}
    
    codes = {}

    def generate_code(node, current_code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code if current_code else '0'
            return
        generate_code(node.left, current_code + "0")
        generate_code(node.right, current_code + "1")

    generate_code(root, "")
    return codes

def compress(input_path, output_path):
    """Compress a text file using Huffman coding"""
    with open(input_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    if not text:
        raise ValueError("Cannot compress empty file")

    root = build_tree(text)
    codes = build_codes(root)

    # Encode the text
    encoded_text = ''.join(codes[char] for char in text)
    
    # Calculate padding
    padding = (8 - len(encoded_text) % 8) % 8
    encoded_text += '0' * padding

    # Convert to bytes
    b = bytearray()
    for i in range(0, len(encoded_text), 8):
        byte = encoded_text[i:i+8]
        b.append(int(byte, 2))

    # Write compressed file
    with open(output_path, 'wb') as out:
        # Store padding info
        out.write(bytes([padding]))
        # Store the Huffman tree using pickle
        pickle.dump(codes, out)
        # Store compressed data
        out.write(b)

def decompress(input_path, output_path):
    """Decompress a Huffman encoded file"""
    with open(input_path, 'rb') as file:
        # Read padding info
        padding = file.read(1)[0]
        
        # Load Huffman codes
        codes = pickle.load(file)
        
        # Read compressed data
        compressed_data = file.read()

    # Reverse the codes dictionary
    reversed_codes = {v: k for k, v in codes.items()}
    
    # Convert bytes to bit string
    bit_string = ''.join(f'{byte:08b}' for byte in compressed_data)
    
    # Remove padding
    if padding > 0:
        bit_string = bit_string[:-padding]

    # Decode the bit string
    decoded_text = ''
    current_bits = ''
    
    for bit in bit_string:
        current_bits += bit
        if current_bits in reversed_codes:
            decoded_text += reversed_codes[current_bits]
            current_bits = ''

    # Write decompressed file
    with open(output_path, 'w', encoding='utf-8') as out:
        out.write(decoded_text)