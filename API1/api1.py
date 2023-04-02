from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({'Hello': 'World'})

phonedict = {'Darek': '730024799', 'Devil': '666666666', 'Trump': '123456789'}

@app.route('/phonebook/get/<string:name>')
def phonebook_get(name):
    if name in phonedict:
        return jsonify({name: phonedict[name]})
    return jsonify({name: None})

@app.route('/phonebook/set/<string:name>')
def phonebook_set(name, number):
    phonedict[name] = number
    return jsonify({'Successful': True})

@app.route('/phonebook/remove/<string:name>')
def phonebook_remove(name):
    if name in phonedict:
        phonedict.pop(name)
        return jsonify({'Successful': True})
    return jsonify({'Successful': False})

@app.route('/phonebook/verify/<string:name>/<string:number>')
def phonebook_verify(name, number):
    return({"Verified": name in phonedict and phonedict[name] == number})

app.run(debug=True)
