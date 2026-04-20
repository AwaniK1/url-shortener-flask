from flask import Flask, render_template, request

import string
import random
from database import create_db

create_db()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['original_url']
        short_code = generate_short_code()
        return f'original url: {url} | short code: {short_code}'
        
    else:
        return render_template('index.html')

def generate_short_code():
    characters = string.ascii_letters + string.digits
    code = ''
    for i in range(6):
        code += random.choice(characters)
    return code

if __name__ == '__main__':
    app.run(debug=True)