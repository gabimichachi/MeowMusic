from flask import Flask, render_template
import mysql.connector
from model.musicas import recuperar_musicas
from model.generos import recuperar_generos 
from model.musicas import adicionar_musica

app = Flask(__name__)


@app.route("/")
@app.route("/principal" , methods =["GET"])
def pagina_principal():
    # recuperando as musicas
    musicas = recuperar_musicas()
    # recuperando os generos
    generos = recuperar_generos()
    # mostrando a pagina
    return render_template("principal.html", musicas = musicas, generos = generos)



@app.route("/admin")
def pag_admin():
    # recuperando as musicas
    musicas = recuperar_musicas()
    # mostrando a pagina 
    return render_template("administracao.html" , musicas = musicas)

@app.route("/musica/post", methods = ["POST"])
def api_inserir_musica():
    nome_musica = request.form.get("titulo_input")
    cantor = request.form.get("")

if adicionar_musica:

    if __name__ == "__main__":
        app.run(debug=True)