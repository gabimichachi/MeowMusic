from database.conexao import conectar 

def recuperar_musicas(ativos: bool=False):
    #passo 1 e 2 já feito
    conexao, cursor = conectar()

    #executando a consulta
    if ativos == False: 
        cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, ativo  FROM musica")

    else:
         cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, ativo  FROM musica WHERE ativo = 1")

    #recuperando os dados
    musicas = cursor.fetchall()

    #fechar a conexão
    conexao.close()

    return musicas 

def adicionar_musica(cantor:str, nome_musica:str, duracao:str, imagem:str, genero:str) -> bool:
    """
    essa função é para adicionar musicas no banco de dados 

    """

    conexao, cursor = conectar()

    cursor.execute("""
                   INSERT INTO Musica
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

    return True

def excluir_musica(codigo:int):
    """
    essa função serve para excluir as músicas do banco de dados    
    """
    conexao, cursor = conectar()


    cursor.execute("""
                   DELETE FROM Musica WHERE Codigo = %s;

""", [codigo])
    

    
def ativar_musica(codigo:int, status:bool):
    """
    essa função serve para alterar as músicas
    """
    conexao, cursor = conectar()
    cursor.execute("""
                ALTER TABLE FROM Musica WHERE Codigo = %s;
""", [codigo])
    


    
    #confirmando o delete
    conexao.commit()

    #fechando a conexao
    conexao.close()

# def ativar_musica(codigo:int, status:bool):

     