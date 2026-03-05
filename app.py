from flask import Flask, render_template, request, redirect
import mysql.connector
from model.musicas import recuperar_musicas
from model.generos import recuperar_generos 
from model.musicas import adicionar_musica
from model.musicas import excluir_musica
from model.usuario import cadastrar_usuario
app = Flask(__name__)


@app.route("/")
@app.route("/principal" , methods =["GET"])
def pagina_principal():
    # recuperando as musicas
    musicas = recuperar_musicas(True)
    # recuperando os generos
    generos = recuperar_generos()
    # mostrando a pagina
    excluir_musica(True)
    return render_template("principal.html", musicas = musicas, generos = generos)



@app.route("/admin")
def pag_admin():
    # recuperando as musicas
    musicas = recuperar_musicas()
    # mostrando a pagina 
    return render_template("administracao.html" , musicas = musicas)

@app.route("/musica/post", methods = ["POST"])
def api_inserir_musica():
    cantor = request.form.get("cantor_input")
    nome_musica = request.form.get("musica_input")
    genero = request.form.get("nome_genero_input")
    duracao = request.form.get("duracao_input")
    url = request.form.get("url_imagem_input")

    if adicionar_musica (cantor, nome_musica, duracao, url, genero):
        return redirect("/admin")
    
    else:
        return ("ERRO AO ADICIONAR MÚSICA")
    
@app.route("/musica/delete/<codigo>")
def apagar_musica(codigo):
    excluir_musica(codigo)
    return redirect("/admin")


@app.route("/cadastro")
def pagina_cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro", methods = ["POST"])
def rota_cadastro_usuario():
    login = request.form.get("usuario")
    senha = request.form.get("senha")
    cadastrar_usuario(login, senha)
    return redirect("/cadastro")


@app.route()






























if __name__ == "__main__":
    app.run(debug=True)