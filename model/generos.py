from database.conexao import conectar 

def recuperar_generos():
    conexao, cursor = conectar()
    cursor.execute("SELECT * from Genero;")

    #rec os dados
    generos = cursor.fetchall()

    #fechando a conexao
    conexao.close()

    return generos