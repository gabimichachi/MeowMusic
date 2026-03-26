from flask import Flask, render_template, request, redirect, session
from model.musicas import recuperar_musicas, adicionar_musica, excluir_musica
from model.generos import recuperar_generos 
from model.usuario import cadastrar_usuario, verificar_usuario
from model.musicas import ativar_musica 

app = Flask(__name__)
app.secret_key = "finnteamo"

@app.route("/home", methods=["GET"])
@app.route("/")
def pagina_principal():
    # recuperando as musicas 
    musicas = recuperar_musicas(True)
    # recuperando os generos 
    generos = recuperar_generos()
    # mostrando a pagina 
    return render_template("principal.html", musicas = musicas, generos = generos)

@app.route("/admin")
def pag_admin():
    if "usuario_logado" not in session:
        return redirect("/login")
    
    # recuperando as muicas 
    musicas = recuperar_musicas()
    generos = recuperar_generos()
    # mostrando a pagina 
    return render_template ("administracao.html", musicas = musicas, generos = generos )

@app.route("/musica/post", methods=["POST"])
def api_inserir_musica():
    nome_musica = request.form.get("musica_nome")
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    url = request.form.get("imagem")
    genero_nome = request.form.get("genero_nome")

    if adicionar_musica( cantor, nome_musica, duracao, url, genero_nome):
        return redirect ("/admin")
    else:
        return ("erro ao adicionar musica")


@app.route("/musica/delete/<codigo>")
def deletar_musica(codigo):
    excluir_musica(codigo)
    return redirect("/admin")

@app.route("/musica/ativar/<codigo>/<status>")
def ativando_musica(codigo, status):
    ativar_musica(codigo, status)
    return redirect("/admin")

@app.route("/cadastrar")
def pag_cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar/post", methods=["POST"])
def cadastro_usuario():
    login = request.form.get("usuario")
    senha = request.form.get("senha")
    cadastrar_usuario(login, senha)
    return redirect("/admin")


@app.route("/login")
def pag_login():
    return render_template("login.html")

@app.route("/login/post", methods=["POST"])
def login_post():
    login = request.form.get("usuario")
    senha = request.form.get("senha")
    usuario = verificar_usuario(login, senha)

    if usuario:
        session["usuario_logado"] = usuario
        return redirect("/admin")
    else:
        return redirect("/login")
    
if __name__ == "__main__":
    app.run(debug=True)