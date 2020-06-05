from flask import Flask, request, render_template, url_for, jsonify
app = Flask(__name__)
MCD = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
       'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
       '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
       '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
       }


def decryption(message):
    message += ' '
    decipher = ''
    mycitext = ''
    for myletter in message:
        if (myletter != ' '):
            i = 0
            mycitext += myletter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MCD.keys())[list(MCD.values()).index(mycitext)]
                mycitext = ''
    return decipher


@app.route('/', methods=["GET", "POST"])
def homepage():
    return render_template('index.html')


@app.route('/api/get', methods=["post"])
def api():
    braille = request.get_json()["braille"]
    print(braille)
    return jsonify(decryption(braille))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
