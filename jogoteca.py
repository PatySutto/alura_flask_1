from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1= Jogo('Tetris', 'Puzzle', 'Atari')
jogo2= Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')

lista_jogos = [jogo1, jogo2, jogo3]

# se refere a este arquivo
app = Flask(__name__)
app.secret_key = 'askjdisad'


@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Jogos', jogos = lista_jogos)


@app.route('/cadastro_jogo')
def cadastro_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')

    return render_template('cadastro_jogo.html', titulo = 'Cadastro de jogos')
 

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)

    lista_jogos.append(jogo)

    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado.')
        return redirect('/')
    
    else:
        flash('Não foi possivel fazer login.' )
        return redirect('/login')
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado.')

    return redirect('/login')
# rodar a aplicação
#app.run(host='0.0.0.0', port=8080)
app.run(host='0.0.0.0', port=8080, debug=True)
