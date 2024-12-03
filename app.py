from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, doc='/docs')

livros = [
    {
        'id': 2,
        'titulo': 'Dom Casmurro',
        'autor': 'Machado de Assis',
        'ano': '1899'
    },
    {
        'id': 3,
        'titulo': 'Memórias Póstumas de Brás Cubas',
        'autor': 'Machado de Assis',
        'ano': '1881'
    },

    {
        'id': 4,
        'titulo': 'Grande Sertão: Veredas',
        'autor': 'João Guimães Rosa',
        'ano': '1956'
    },

]






#Rota mostrar a lista de livros cadastrados
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)



# Rota para buscar o livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def consultar_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)



# Rota editar um livro na API
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_no_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Rota para adicionar um novo livro
@app.route('/livros', methods=['POST'])
def incluir_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro)


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)




#Rodar a API
app.run(port=5001, host='localhost', debug=True)
