from flask import Flask
from flask import render_template
from flask import request

from encoder import EncryptionHandler

app = Flask(__name__)


@app.route('/')
def main_page():
    e = EncryptionHandler()
    return render_template("index.html", cipher_types=sorted(e.codes.keys()))


@app.route('/', methods=['POST'])
def apply_text():
    encryption_handler = EncryptionHandler()
    cipher_details = {'text_to_cipher': request.form.get('text_to_cipher'),
                      'cipher_type': request.form.get('cipher_type_selector'),
                      'cipher_args': request.form.get('argument_for_cipher'),
                      }

    encoded_text = ' '.join(encryption_handler.apply_cipher(**cipher_details))
    return render_template('index.html', encoded=encoded_text, text_to_encode=cipher_details.get('text_to_cipher'),
                           cipher_types=sorted(encryption_handler.codes.keys()),
                           cipher_args=cipher_details.get('cipher_args'))


if __name__ == '__main__':
    app.run(debug=True)
