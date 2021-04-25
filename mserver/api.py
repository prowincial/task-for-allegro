import json
import requests
from flask import jsonify, make_response, abort, Blueprint

github_urls = {
    "user": "https://api.github.com/users/{0}",
    "user_repos": "https://api.github.com/users/{0}/repos",
}

bp = Blueprint("api", __name__, url_prefix="/api/v0.1")


def github_request(url):
    try:
        response = requests.get(url)
    except requests.ConnectionError:
        return "Connection Error"
    return json.loads(response.text)


@bp.route('/<string:username>/repos', methods=['GET'])
def get_tasks(username):
    """
    Returns briefed information about user repositories and their stars

    :param username: str
    :return: JSON object with data

    Url template: http://hostname/api/v0.1/allegro/repos
    Url example: https://127.0.0.1:5000/api/v0.1/allegro/repos
    """
    print(f"Username = {username}")
    if user_exists(username):
        tasks = github_request(github_urls['user_repos'].format(username))
    else:
        abort(404)
    return jsonify(list(map(make_good_format, tasks)))


@bp.route('/<string:username>/stargazers', methods=['GET'])
def get_stars(username):
    """
    Returns total number of all stars in user repositories

    :param username: str
    :return: JSON object with data

    Url template: http://hostname/api/v0.1/allegro/stargazers
    Url example: https://127.0.0.1:5000/api/v0.1/allegro/stargazers
    """
    if user_exists(username):
        tasks = github_request(github_urls['user_repos'].format(username))
    else:
        abort(404)
    stars_sum = sum(task['stargazers_count'] for task in tasks)
    return jsonify({'stargazers_count': stars_sum})


@bp.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'User not found'}), 404)


def user_exists(username):
    return 'message' not in (github_request(github_urls['user'].format(username))).keys()


def make_good_format(task):
    new_task = {x: task[x] for x in task if x in ('name', 'stargazers_count')}
    return new_task
