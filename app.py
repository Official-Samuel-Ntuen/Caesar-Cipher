# ================================
# Caesar Cipher Web App
# DecodeLabs - Project 2
# Flask Backend
# ================================

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result

def brute_force(text):
    results = []
    for shift in range(1, 26):
        results.append({
            "shift": shift,
            "text": decrypt(text, shift)
        })
    return results

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    text = data.get('text', '')
    shift = int(data.get('shift', 3))
    action = data.get('action', 'encrypt')

    if action == 'encrypt':
        result = encrypt(text, shift)
    elif action == 'decrypt':
        result = decrypt(text, shift)
    elif action == 'brute':
        result = brute_force(text)
        return jsonify({"result": result, "action": "brute"})

    return jsonify({"result": result, "action": action})

if __name__ == '__main__':
    import webbrowser
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=True)
    