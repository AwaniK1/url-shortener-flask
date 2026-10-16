
from flask import Flask, render_template, request, redirect, url_for
import string
import random
from urllib.parse import urlparse
import re

from database import (
    create_db,
    insert_url,
    find_url,
    increment_clicks,
    get_clicks,
    find_short_code_by_url
)

app = Flask(__name__)
create_db()


def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


def is_valid_url(url):
    try:
        parsed = urlparse(url)
        hostname = parsed.hostname

        return (
            parsed.scheme in ('http', 'https')
            and bool(hostname)
            and '.' in hostname
            and ' ' not in url
        )
    except ValueError:
        return False



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('original_url', '').strip()
        custom_alias = request.form.get('custom_alias', '').strip()

        if not url:
            return render_template(
                'index.html',
                error='Please enter a URL.'
            )

        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        if not is_valid_url(url):
            return render_template(
                'index.html',
                error='Please enter a valid URL.'
            )

        # Handle a custom alias
        if custom_alias:
            if not re.fullmatch(r'[A-Za-z0-9_-]{3,30}', custom_alias):
                return render_template(
                    'index.html',
                    error='Alias must be 3–30 characters: letters, numbers, _ or -.'
                )

            if find_url(custom_alias):
                return render_template(
                    'index.html',
                    error='This alias is already taken.'
                )

            short_code = custom_alias
            insert_url(url, short_code)

        else:
            # Reuse the code if this URL already exists
            short_code = find_short_code_by_url(url)

            if not short_code:
                short_code = generate_short_code()

                while find_url(short_code):
                    short_code = generate_short_code()

                insert_url(url, short_code)

        return redirect(url_for('show_result', short_code=short_code))

    return render_template('index.html')



@app.route('/result/<short_code>')
def show_result(short_code):
    original_url = find_url(short_code)

    if not original_url:
        return 'Short URL not found', 404

    short_url = request.host_url + short_code

    return render_template(
        'index.html',
        short_url=short_url,
        original_url=original_url,
        clicks=get_clicks(short_code)
    )


@app.route('/analytics/<short_code>')
def analytics(short_code):
    clicks = get_clicks(short_code)

    if clicks is None:
        return {'error': 'Short URL not found'}, 404

    return {'clicks': clicks}


@app.route('/<short_code>')
def redirect_url(short_code):
    original_url = find_url(short_code)

    if original_url:
        increment_clicks(short_code)
        return redirect(original_url)

    return 'Short URL not found', 404


if __name__ == '__main__':
    app.run(debug=True)
