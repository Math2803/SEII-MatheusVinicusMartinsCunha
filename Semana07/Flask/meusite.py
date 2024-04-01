from flask import Flask, render_template, request
from ramdom import randint
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
	variavel = "Game: Adivinhe o numero correto"
	if request.methods == "GET":
		return render_template('index.html', variavel = variavel)
	else:
		numero = randint(1,20)
		palpite = int(request.form.get("name"))
		if numero == palpite:
			return '<h1>Resultado: Você ganhou</h1>'
		else:
			return '<h1>Resultado: Você perdeu</h1>'

@app.route('/<string:nome>')
def error(nome):
	variavel = f'<h1>Pagina({nome} não existe)</h1>'
	return render_template("error.html",variavel = variavel)
