from flask_restful import Resource, request
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    # insere nova habilidade na lista
    def post(self):
        nova_habilidade = json.loads(request.data)
        lista_habilidades.append(nova_habilidade)

    # a partir de um id, vai alterar o nome da habilidade naquela posicao
    def put(selfs, id):
        posicao = len(lista_habilidades)
        nova_habilidade = json.loads(request.data)
        lista_habilidades[posicao] = nova_habilidade

    # deletar uma habilidade na posicao indicada
    def delete(self, id):
        del lista_habilidades[id]