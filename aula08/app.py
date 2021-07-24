from flask import Flask, render_template, redirect,request

app = Flask(__name__)  # instanciando objeto
itens = list()
@app.route('/') #Toda rota requer uma função ; Rota principal 
def index():
    return render_template('index.html', titulo='Lista', itens=itens)

@app.route('/new', methods=['POST', 'GET'])
def new():
    if request.method =='POST':
        item = request.form['item']
        itens.append(item)
        return redirect('/')

@app.route('/clear')
def clear():
    itens.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)