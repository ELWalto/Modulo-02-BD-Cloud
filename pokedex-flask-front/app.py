from flask import Flask, render_template, redirect, request,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  #instanciando objeto 'APP' 
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://sfgworrf:uCpELVO6PpPhWsIpCxcnSfdVTd7iVegU@kesavan.db.elephantsql.com/sfgworrf' #Configurando a URL do Elephant  para o BD SQLAlchemy Lembrando de colocar o QL no postgresql.PARA MUDAR PARA O SQLITE MUDA SÓ A URL 'SQLITE:///POKEDEX.SQLITE3'
db = SQLAlchemy(app) #DB recebe o aplicativo para o SQLAlchemy

class Pokemon(db.Model): #  a classe POKEMON Virou uma tabela modelo no banco de dados
    id = db.Column(db.Integer, autoincrement=True, primary_key=True) # Criando uma coluna com ID autoincrement e como chave primaria
    nome = db.Column(db.String(150), nullable = False)  # Criando uma coluna com nome  String e campo não nulo
    imagem = db.Column (db.String(500), nullable = False) # Criando uma coluna com nome  String e campo não nulo
    descricao = db.Column (db.String(500), nullable = False) # Criando uma coluna com nome  String e campo não nulo
    tipo = db.Column (db.String(150), nullable = False) # Criando uma coluna com nome  String e campo não nulo

    def __init__(self, nome, imagem, descricao, tipo): # Função construtora  passando os parametros das tabelas do banco de dados
        self.nome = nome
        self.imagem = imagem
        self.descricao = descricao
        self.tipo = tipo


@app.route('/') # criação da rota principal
def index():
    pokedex = Pokemon.query.all() # Pegando todas linhas dos pokemons em lista 
    return render_template('index.html',pokedex = pokedex) #rendriza o template do index.html 

@app.route('/add', methods=['GET','POST'])
def new():
    if request.method == 'POST': # verificando se o metodo é o post para evitar que o usuário acesse a rota pela url
        pokemon = Pokemon(request.form['nome'], # criando objeto pokemon da Clase Pokemon
        request.form['imagem'],
        request.form['descricao'],
        request.form['tipo'])

        db.session.add(pokemon) # insert na tabela
        db.session.commit() # Confirmando a alteração da tabela ### ENTER ###
        return redirect('/')

@app.route('/edit/<id>', methods=['GET','POST'])
def edit(id):
    pokemon = Pokemon.query.get(id) #pokemon recebe uma pesquisa no banco completo pelo id e faz com que o modal de edição apareça
    pokedex = Pokemon.query.all() # pokedex traz todos os pokemons cadastrados
    if request.method == 'POST': # verificando se o metodo é post para evitar que o usuário acesse pela url, se verdadeiro ele entra no if do editar e atualiza as informações
        pokemon.nome = request.form['nome'],
        pokemon.descricao = request.form['descricao']
        pokemon.imagem = request.form['imagem']
        pokemon.tipo = request.form['tipo']
        db.session.commit() 
        return redirect('/')

    return render_template('index.html', pokemon = pokemon , pokedex=pokedex) #rendriza o template index.html trazendo as variaveis pokemon e pokedex ja cadastradas no BD
    
@app.route('/<id>') # rota para pegar o pokemon por id e habilitar a deleção
def get_by_id(id):
    pokemon = Pokemon.query.get(id)
    pokedex = Pokemon.query.all()
    return render_template('index.html', pokemonDelete = pokemon , pokedex=pokedex)

@app.route('/delete/<id>') # Rota para deletar efetivamente um pokemon cadastrado pelo id que vem do modal sim 
def delete(id): 
    pokemon = Pokemon.query.get(id) # pega o pokemon pelo id
    db.session.delete(pokemon) #deleta o pokemon
    db.session.commit() # confirma a deleção
    return redirect('/') # redireciona para a rota principal

@app.route('/filter',methods=['GET', 'POST'])
def filter():
    tipo = request.form['search']
    pokedex = Pokemon.query.filter(Pokemon.tipo.ilike(f'%{tipo}%')).all()
    return render_template('index.html', pokedex =pokedex)

@app.route('/filter/<param>')
def filter_by(param):
    pokedex = Pokemon.query.filter_by(tipo=param).all()
    return render_template('index.html',pokedex = pokedex)


if __name__ == '__main__': 
    db.create_all() # Verifica se existe a tabela se não existir ele cria .
    app.run(debug=True) #usando o debug=True Ele atualiza o servidor flask local automaticamente posso alterar a porta usando port = xxx (numero porta)

