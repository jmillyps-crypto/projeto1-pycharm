from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return 'Olá Mundo'


@app.route('/ola')
def ola():
    return 'Bem vindo, hj vai ser muito legal'

@app.route('/nome')
def nome():
    nome = 'Jaja'
    return render_template('index.html',nome=nome)


@app.route('/nomes')
def nomes():
    nomes = ['Pereira', 'Rafael',  'Alefe']
    return render_template('nomes.html',lista=nomes)



@app.route('/alunos')
def alunos():
    alunos = ['Vitória', 'Jamily', 'Malu']
    return render_template('alunos.html', alunos=alunos)

if __name__ == '__main__':
    app.run(debug=True)