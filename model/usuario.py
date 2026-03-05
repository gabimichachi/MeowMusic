from database.conexao import conectar

def cadastrar_usuario(login:str, senha:str):
    conexao, cursor = conectar()

    cursor.execute("""
                   INSERT INTO MeowMusic.login
                        (usuario, 
                        senha)
                   VALUES
                   (%s,
                   %s);

                   """, 
                   
                   [login, senha]
                   )

    conexao.commit()
    conexao.close()