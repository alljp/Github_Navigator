import requests
from flask import Flask, render_template, request, json

BASE_URL = 'https://api.github.com'

app = Flask(__name__, template_folder='')


def get_latest_commit(repo):
    url = BASE_URL + '/repos/' + repo['full_name'] + '/commits'
    response = requests.get(url)
    commits = json.loads(response.content)
    repo['latest_commit'] = commits[0]
    return repo


def get_newest_repos(search_term):
    url = BASE_URL + '/search/repositories'
    response = requests.get(url, params={'q': search_term})
    repos = json.loads(response.content)['items']
    latest_repos = sorted(repos, key=lambda k: k.get(
        "created_at", 0), reverse=True)[:5]
    return map(get_latest_commit, latest_repos)


@app.route('/navigator')
def list_repos():
    search_term = request.args.get('search_term', None)
    repos = get_newest_repos(search_term)
    return render_template('template.html',
                           search_term=search_term, repos=repos)


if __name__ == '__main__':
    app.run(port=9876)
