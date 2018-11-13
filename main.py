from flask import Flask, jsonify
from flask_basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'user'
app.config['BASIC_AUTH_PASSWORD'] = 'password'
app.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(app)

actors = [
    {'id': 1, 'actor': 'William Shatner', 'role': 'James T'},
    {'id': 2, 'actor': 'Leonard Nimoy', 'role': 'Spock'},
    {'id': 3, 'actor': 'DeForest Kelley', 'role': 'Leonard McCoy'},
    {'id': 4, 'actor': 'James Doohan', 'role': 'Montgomery Scott'},
    {'id': 5, 'actor': 'George Takei', 'role': 'Hikaru Sulu'},
    {'id': 6, 'actor': 'Walter Koenig', 'role': 'Pavel Chekov'},
    {'id': 7, 'actor': 'Nichelle Nichols', 'role': 'Nyota Uhura'},
    {'id': 8, 'actor': 'Majel Barrett', 'role': 'Christine Chapel'}
]


def find(xs, f):
    ys = list(filter(f, xs))
    if not ys:
        return None
    else:
        return ys[0]


def cata(value, default):
    if value[0]:
        return value
    else:
        return default


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/version', methods=['GET'])
def get_version():
    return jsonify({'version': 'GCE-docker-2.0.0'}), 200


@app.route('/actors', methods=['GET'])
def get_persons():
    return jsonify(actors), 200


@app.route('/actors/<int:id>', methods=['GET'])
def get_actor_by_id(id: int):
    x = find(actors, lambda x: x['id'] == id)
    body, code = cata((x, 200), ({'error': f'actor with id={id} not found'}, 404))
    return jsonify(body), code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
