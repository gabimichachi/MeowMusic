from database.conexao import conectar

def recuperar_musicas():
    #passo 1 e 2 já feito
    conexao, cursor = conectar()

    #executando a consulta
    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem FROM musica")

    #recuperando os dados
    musicas = cursor.fetchall()

    #fechar a conexão
    conexao.close()

    return musicas 

