from flask import Flask, jsonify, request, abort
from Prototype import Network

app = Flask(__name__)

cache = {}
cache['last'] = 0
cache['networks'] = {}

@app.route('/network', methods=['GET'])
def get_networks():
    for idx, elem in enumerate(cache['network']):
        liste.append([idx, elem])
    return jsonify({'resultat': liste}), 201

@app.route('/network/<network_id>', methods=['GET'])
def get_network(network_id):
    elem = cache['network'][network_id]
    return jsonify({'resultat': elem}), 201

@app.route('/network/create', methods=['POST'])
def post_network():
    if not request.json or not 'inputType' in request.json or not 'classes' in request.json:
        abort(400)
    count = 0
    cache['network'][cache['last']] = {}
    cache['network'][cache['last']]['titre'] = request.json.titre
    if len(request.json.words) > 0:
        cache['network'][cache['last']]['words'] = []
        for elem in request.json.words:
            count+=1
            cache['network'][cache['last']]['words'].append(elem)
    cache['network'][cache['last']]['inputType'] = []
    for elem in request.json.inputType:
        count+=1
        cache['network'][cache['last']]['inputType'].append(elem)
    cache['network'][cache['last']]['tag'] = []
    for elem in request.json.tag:
        cache['network'][cache['last']]['tag'].append(elem)
    count-=1
    cache['network'][cache['last']]['classes'] = []
    for elem in request.json.classes:
        cache['network'][cache['last']]['classes'].append(elem)
    cache['network'][cache['last']]['network'] = Network(count, len(request.json.classes))
    cache['network'][cache['last']]['samples'] = []
    cache['last']+=1
    return jsonify({'resp': "Cree!"}), 201

@app.route('/network/<network_id>/sample', methods=['POST'])
def post_sample(network_id):
    if not request.json or not 'inputs' in request.json or not 'result' in request.json:
        abort(400)
    cache['network'][network_id]['samples'].append([request.json['inputs'], request.json['result']])
    return jsonify({'donnee': cache['network'][network_id]['samples'][len(cache["sample"]) - 1]}), 201

@app.route('/network/<network_id>/test', methods=['POST'])
def post_test(network_id):
    if not request.json or not 'inputs' in request.json:
        abort(400)
    cache['network'][network_id]['network'].train(cache['network'][network_id]['sample'])
    cache['network'][network_id]['network'].test(request.json['inputs'])
    return jsonify({'resultat': cache['network'][network_id]['network'].resultatActuel}), 201



if __name__ == '__main__':
    app.run(debug=True)
