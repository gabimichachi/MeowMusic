import mysql.connector


def conectar():
    tipo_conexao = "NUVEM"
    if tipo_conexao == "LOCAL":
    #conectando no banco de dados
        conexao = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "MeowMusic"
    )

        conexao = mysql.connector.connect(
        host = "servidor-gabrielli-servidor-gabimichachi.a.aivencloud.com",
        port = 23981,
        user = "avnadmin",
        password = "AVNS_ubgslKrmQbAMk4HCkmb",
        database = "MeowMusic"
    )
    #criando o cursor
    cursor = conexao.cursor(dictionary=True)

    return conexao, cursor
