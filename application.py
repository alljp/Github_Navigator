import requests
from flask import Flask, render_template, request

BASE_URL = 'https://api.github.com'

app = Flask(__name__, template_folder='')


@app.route('/navigator')
def list_repos():
    search_term = request.args.get('search_term', None)
    return render_template('template.html', search_term=search_term)


if __name__ == '__main__':
    app.run(port=9876)
