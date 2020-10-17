from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, lista_habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {   'id':0,
        'nome':'roberto',
        'habilidades': ['Python', 'Flask']},
    {   'id':1,
        'nome':'lopes',
        'habiliades': ['Python', 'Django']}
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': f'desenvolvedor de id {id} nao existe'}
        except Exception:
            response = {'status': 'erro', 'mensagem': 'erro desconhecido'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        print(dados['habilidades'])
        print(lista_habilidades)
        resultado = [True for item in dados['habilidades'] if item in lista_habilidades]
        if False in lista_habilidades:
            return {'message': 'dados nao alterados'}
        else:
            desenvolvedores[id] = dados
            return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'registro excluido'}
    
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)