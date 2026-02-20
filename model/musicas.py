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

def adicionar_musica(cantor:str, nome_musica:str, duracao:str, imagem:str, genero:str) -> bool:
    """
    a função é adicionar musicas no banco de dados 

    """

    conexao, cursor = conectar()

    cursor.execute("""
                   INSERT INTO musica
                   (CANTOR, NOME, DURACAO, URL_IMAGEM, NOME_GENERO)
                   VALUES
                   (%s,%s,%s,%s,%s);
                   """,
                   [cantor, nome_musica, duracao, imagem, genero]
                   )
    
    # values = valores

    #confirmando o insert
    conexao.commit()

    conexao.close()