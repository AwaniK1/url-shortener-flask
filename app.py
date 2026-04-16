from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['original_url']
        return f'original url: {url}'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug='True')