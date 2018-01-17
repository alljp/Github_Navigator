import requests
from flask import Flask, render_template

BASE_URL = 'https://api.github.com'

app = Flask(__name__, template_folder='')


@app.route('/navigator')
def list_repos():
    return "Hello"


if __name__ == '__main__':
    app.run(port=9876)
