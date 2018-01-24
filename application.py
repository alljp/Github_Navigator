import requests
from flask import Flask, render_template, request, json

BASE_URL = 'https://api.github.com'

app = Flask(__name__, template_folder='')


def parse_and_check(content):
    """
    Try and parse the JSON returned from GitHub API and raise an exception if there is any error.
    Also check for errors due to  some GitHub API network outages or rate limits
    """

    try:
        data = json.loads(content.decode('utf-8'))
        if 'message' in data:
            if data['message'] == 'Git Repository is empty.':
                return None
            raise Exception(data['message'])
        return data
    except ValueError:
        raise Exception('Unknown error: ' + content)


def get_latest_commit(repo):
    """
    Gets the commits for a repo, and load the latest commit to it.
    """

    url = BASE_URL + '/repos/' + repo['full_name'] + '/commits'
    response = requests.get(url)
    commits = parse_and_check(response.content)
    if commits is None:
        return repo
    repo['latest_commit'] = commits[0]
    return repo


def get_newest_repos(search_term):
    """
    Get the first page of results returned by the GitHub search API, sort 
    them according to the date of creation, and return the latest 5 repos
    """

    url = BASE_URL + '/search/repositories'
    response = requests.get(url, params={'q': search_term})
    repos = parse_and_check(response.content)['items']
    latest_repos = sorted(repos, key=lambda k: k.get(
        "created_at", 0), reverse=True)[:5]
    if latest_repos:
        return map(get_latest_commit, latest_repos)
    return None


@app.route('/navigator')
def list_repos():
    search_term = request.args.get('search_term', None)
    try:
        if not search_term:
            raise Exception('Search term is required')
        repos = get_newest_repos(search_term)
        return render_template('template.html',
                               search_term=search_term, repos=repos)
    except Exception as error:
        return str(error)

if __name__ == '__main__':
    app.run(port=9876)
