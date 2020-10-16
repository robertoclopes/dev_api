from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {   'id':0,
        'nome':'roberto',
        'habilidades': ['Python', 'Flask']},
    {   'id':1,
        'nome':'lopes',
        'habiliades': ['Python', 'Django']}
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro', 'mensagem': f'desenvolvedor de id {id} nao existe'}
        except Exception:
            response = {'status':'erro', 'mensagem': 'erro desconhecido'}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'registro excluido'})

@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedor)


if __name__ == '__main__':
    app.run(debug=True)