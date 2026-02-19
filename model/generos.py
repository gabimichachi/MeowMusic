from database.conexao import conectar 

def recuperar_generos():
    conexao, cursor = conectar()
    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")

    #rec os dados
    generos = cursor.fetchall()

    #fechando a conexao
    conexao.close()

    return generos