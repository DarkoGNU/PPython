import collections
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({'Hello': 'World'})


people = {
    'Darek': {'name': 'Darek', 'number': '730024799', 'car': True, 'friends': ['Devil', 'Trump']},
    'Devil': {'name': 'Devil', 'number': '666666666', 'car': True, 'friends': []},
    'Trump': {'name': 'Trump', 'number': '123456789', 'car': False, 'friends': ['Devil']},
    'Osoba1': {'name': 'Osoba1', 'number': '000000000', 'car': False, 'friends': []},
    'Osoba2': {'name': 'Osoba2', 'number': '000000000', 'car': False, 'friends': ['Osoba1', 'Darek']},
    'Osoba3': {'name': 'Osoba3', 'number': '000000000', 'car': False, 'friends': ['NoPerson']},
    'Osoba4': {'name': 'Osoba4', 'number': '000000000', 'car': False, 'friends': ['Osoba6']},
    'Osoba5': {'name': 'Osoba5', 'number': '000000000', 'car': False, 'friends': ['Osoba3', 'Osoba2']},
    'Osoba6': {'name': 'Osoba6', 'number': '000000000', 'car': False, 'friends': []},
    'Osoba7': {'name': 'Osoba7', 'number': '000000000', 'car': False, 'friends': ['Osoba5']},
    'Osoba8': {'name': 'Osoba8', 'number': '000000000', 'car': False, 'friends': ['Osoba7', 'Osoba6']},
    'Osoba9': {'name': 'Osoba9', 'number': '000000000', 'car': False, 'friends': ['Trump', 'Osoba4']},
}


@app.route('/carbook/bfs/<string:key>')
def carbook(key):
    if key not in people:
        return jsonify({'Status': 'person not found'})

    seen, queue = set([key]), collections.deque([key])

    while queue:
        vertex = queue.popleft()
        if vertex not in people:
            continue
        vertex = people[vertex]

        if vertex['car'] == True:
            return vertex

        for friend in vertex['friends']:
            if friend not in seen:
                seen.add(friend)
                queue.append(friend)

    return jsonify({'Status': 'no friends with car found'})


@app.route('/phonebook/<string:key>', methods=['GET', 'PUT', 'DELETE'])
def phonebook(key):
    print(people)

    if request.method == 'GET':
        if key in people:
            return jsonify({key: people[key]})
        return jsonify({key: None})

    elif request.method == 'PUT':
        people[key] = request.get_json(force=True)
        return jsonify({'Status': 'Success'})

    elif request.method == 'DELETE':
        if key not in people:
            return jsonify({'Status': 'resource does not exist'})

        people.pop(key)
        return jsonify({'Status': 'Success'})


@app.route('/phonebook', methods=['POST'])
def phonebook_post():
    data = request.get_json(force=True)

    if data['name'] in people:
        return jsonify({'Status': 'resource exists'})

    people[data['name']] = data
    return jsonify({'Status': 'Success'})


app.run(debug=True)
