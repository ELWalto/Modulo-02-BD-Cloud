from flask import Flask, render_template, redirect, request, flash, session
from flask_mail import Mail, Message #Importa o Mail e o Message do flask_mail para facilitar o envio de emails#
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Secret'

# Configuração do envio de email.
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'form.sitewalter@gmail.com',
    "MAIL_PASSWORD": 'Wc02ck06'
}

app.config.update(mail_settings) #atualizar as configurações do app com o dicionário mail_settings
mail = Mail(app) # atribuir a class Mail o app atual.

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nftrzaie:jiLp26A8PKVyn_OsId6gKRoEw3u0Mihc@kesavan.db.elephantsql.com/nftrzaie'

db = SQLAlchemy(app)

#Classe para capturar as informações do formulário de forma mais organizada
class Contato:
   def __init__ (self, nome, email, mensagem):
      self.nome = nome
      self.email = email
      self.mensagem = mensagem

class Projeto(db.Model):
   id = db.Column (db.Integer, primary_key = True, autoincrement = True)
   nome = db.Column (db.String(150), nullable = False )
   imagem = db.Column (db.String(500), nullable = False)
   descricao = db.Column (db.String(500), nullable = False)
   link = db.Column(db.String(500), nullable = False)
   
   def __init__(self,nome, imagem, descricao, link):
      self.nome = nome
      self.imagem = imagem
      self.descricao = descricao
      self.link = link





# Rota principal apenas para renderizar a página principal.
@app.route('/')
def index():
   session['user_logado'] = None
   projetos = Projeto.query.all()
   return render_template('index.html', projetos = projetos)

@app.route('/adm')
def adm():
   if 'user_logado' not in session or session['user_logado'] == None:
      flash('faça o login')
      return redirect('/login')
   projetos = Projeto.query.all()
   return render_template('adm.html', projetos = projetos)

@app.route('/new', methods=['GET', 'POST'])
def new():
   if request.method == 'POST': # Verifica se o metodo recebido na requisição é POST
      # cria o objeto projeto, adiconando os campos do form nele.
      projeto = Projeto(
         request.form['nome'],
         request.form['imagem'],
         request.form['descricao'],
         request.form['link']
      )
      db.session.add(projeto) # Adiciona o objeto projeto no banco de dados.
      db.session.commit() # Confirma a operação
      flash('Projeto criado com sucesso!') # Mensagem de sucesso.
      return redirect('/adm') # Redireciona para a rota adm

#Crud - Delete#
@app.route('/delete/<id>') 
def delete(id):
   projeto = Projeto.query.get(id) # Busca um projeto no banco através do id
   db.session.delete(projeto) # Apaga o projeto no banco de dados
   db.session.commit() # Confirma a operação
   return redirect('/adm') #Redireciona para a rota ad
#crud autenticação e login#
@app.route('/login')
def login():
   session['usuario_logado'] = None # Desloga o usuario
   return render_template('login.html')


@app.route('/auth', methods=['GET', 'POST']) # Rota de autenticação
def auth():
   if request.form['senha'] == 'admin': # Se a senha for 'admin' faça:
      session['usuario_logado'] = 'admin' # Adiciona um usuario na sessão
      flash('Login feito com sucesso!') # Envia mensagem de sucesso
      return redirect('/adm') # Redireciona para a rota adm
   else: # Se a senha estiver errada, faça:
      flash('Erro no login, tente novamente!')  # Envia mensagem de erro
      return redirect('/login') # Redireciona para a rota login

#Crud- editar

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
   projeto = Projeto.query.get(id) # Busca um projeto no banco através do id
   projetos = Projeto.query.all()
   if request.method == "POST": # Se a requisição for um POST, faça:
      # Alteração de todos os campos de projetoEdit selecionado no get id
      projeto.nome = request.form['nome']
      projeto.descricao = request.form['descricao']
      projeto.imagem = request.form['imagem']
      projeto.link = request.form['link']
      db.session.commit() # Confirma a operação
      return redirect('/adm') #Redireciona para a rota adm
   # Renderiza a página adm.html passando o projetoEdit (projeto a ser editado)
   return render_template('adm.html', projeto=projeto, projetos=projetos) 

#### MODAL ####


### Pegar projeto por id ###
@app.route('/<id>')
def projeto_por_id(id):
   projetoDel = Projeto.query.get(id)
   return render_template('adm.html', projetoDel = projetoDel)
   



# Rota de envio de email.
@app.route('/send', methods=['GET', 'POST'])
def send():
   if request.method == 'POST':
      # Capiturando as informações do formulário com o request do Flask e criando o objeto formContato
      formContato = Contato(
         request.form['nome'],
         request.form['email'],
         request.form['mensagem']
      )

      # Criando o objeto msg, que é uma instancia da Class Message do Flask_Mail
      msg = Message(
         subject = 'Contato do seu Portfólio', #Assunto do email
         sender = app.config.get("MAIL_USERNAME"), # Quem vai enviar o email, pega o email configurado no app (mail_settings)
         recipients = [app.config.get("MAIL_USERNAME")], # Quem vai receber o email, mando pra mim mesmo, posso mandar pra mais de um email.
         # Corpo do email.
         body=f''' {formContato.nome} com o email {formContato.email}, te mandou a seguinte mensagem: 
         
               {formContato.mensagem}''' 
         )
      mail.send(msg) #envio efetivo do objeto msg através do método send() que vem do Flask_Mail
   return render_template('send.html', formContato = formContato) # Renderiza a página de confirmação de envio.

if __name__ == '__main__':
   db.create_all()
   app.run(debug=True)


