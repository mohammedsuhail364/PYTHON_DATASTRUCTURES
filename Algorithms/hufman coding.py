import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
# fre-1,add-620 fre-2 add-ad20
def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def encode_huffman_tree(root, current_code, codes):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        return

    encode_huffman_tree(root.left, current_code + '0', codes)
    encode_huffman_tree(root.right, current_code + '1', codes)

def huffman_encode(text):
    if len(text) == 0:
        return '', {}

    root = build_huffman_tree(text)
    codes = {}
    encode_huffman_tree(root, '', codes)

    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes

def huffman_decode(encoded_text, codes):
    if len(encoded_text) == 0:
        return ''

    decoded_text = ''
    current_code = ''
    for bit in encoded_text:
        current_code += bit
        if current_code in codes.values():
            decoded_text += next((char for char, code in codes.items() if code == current_code), '')
            current_code = ''
    return decoded_text

# Example usage:
text = "hello world"
encoded_text, codes = huffman_encode(text)
print("Encoded text:", encoded_text)
print("Huffman Codes:", codes)
decoded_text = huffman_decode(encoded_text, codes)
print("Decoded text:", decoded_text)
