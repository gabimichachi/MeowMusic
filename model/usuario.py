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


def verificar_usuario(login:str, senha: str) -> list:
    """
    função que verifica se o usuário está cadastrado 
    se estiver cadastrado retorna os dados do usuário
    se não estiver cadastrado retorno None
    """

    conexao, cursor = conectar()
    cursor.execute("SELECT login, senha FROM usuario WHERE login = %s,  and senha = %s", [login, senha])
    usuario = cursor.fetchone()
    conexao.commit()
    conexao.close()
    return usuario