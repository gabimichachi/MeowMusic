from flask import Flask, render_template
import mysql.connector
from model.musicas import recuperar_musicas
from model.generos import recuperar_generos 

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

if __name__ == "__main__":
    app.run(debug=True)