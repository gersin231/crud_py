import mysql.connector
 
class Database():
    def __init__(self, banco="syspython"):
        self.banco = banco
 
    def connect(self):
        self.conn = mysql.connector.connect(
        host='127.0.0.1',
        database=self.banco,
        user='root',
        password=''
        )
 
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado com suceso!")
        else:
            print("Erro!!")
 
    def insert_client(self):
        self.connect()
        try:
            # nome = "Eliandro"
            # cpf = "90909090"
            # login = "eliandro@senha"
            # senha = "senhaElia"
            # fone = "67992997470"
            # cidade = "Campo Grande"
 
            args = ("Eliandro Silva","666","meulogin","333","222","CG")
 
            # self.cursor.execute(f'INSERT INTO cliente (nome,cpf,login,senha,fone,cidade) VALUES ("{nome}","{cpf}","{login}","{senha}","{fone}","{cidade}");')
            self.cursor.execute('INSERT INTO cliente (nome,cpf,login,senha,fone,cidade) VALUES (%s,%s,%s,%s,%s,%s)',args)
            self.conn.commit()
            print("Cliente cadastrado com sucesso!!!")
 
        except Exception as err:
            print(err)
 
    def select_client(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM cliente")
            clientes = self.cursor.fetchall()
            for cli in clientes:
                print(clientes)
 
        except Exception as err:
            print(err)
 
    def select_client_by_id(self,id):
        self.connect()
        # id = 1
        try:
            self.cursor.execute(f"SELECT * FROM cliente WHERE id = {id}")
            cli = self.cursor.fetchone()
            # for cli in clientes:
            # print(cli[0],cli[1],cli[2],cli[2])
            return cli
 
        except Exception as err:
            print(err)
 
    def update_client(self,id):
        self.connect()
        try:
            cliente = list(self.select_client_by_id(id))
            print(cliente)
            # print(cliente)
            # nome = cliente[1]
            # cpf = cliente[2]
            # login = cliente[3]
            # senha = cliente[4]
            # fone = cliente[5]
            # cidade = cliente[6]
 
            # nome2 = input("Digite o NOME: ")
            # cpf2 = input("Digite o CPF: ")
            # login2 = input("Digite o LOGIN: ")
            # senha2 = input("Digite o SENHA: ")
            # fone2 = input("Digite o FONE: ")
            # cidade2 = input("Digite o CIDADE: ")
            # print(cpf)
         
            cliente[1] = input("Digite o novo NOME: ")
            cliente[2] = input("Digite o novo CPF: ")
            cliente[3] = input("Digite o novo LOGIN: ")
            cliente[4] = input("Digite o novo SENHA: ")
            cliente[5] = input("Digite o novo FONE: ")
            cliente[6] = input("Digite o novo CIDADE: ")
 
            self.cursor.execute(f"""
                                UPDATE cliente
                                SET nome = '{cliente[1]}',
                                cpf = '{cliente[2]}',
                                login = '{cliente[3]}',
                                senha = '{cliente[4]}',
                                fone = '{cliente[5]}',
                                cidade = '{cliente[6]}'
                                WHERE id = {cliente[0]}
                                """)
            self.conn.commit()
            cli_atualizado = self.select_client_by_id(cliente[0])
            print("Cliente Atualizado com sucesso!!! ")
            print(cli_atualizado)
 
 
        except Exception as erro:
            print(erro)
 
   
    def delete_client(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cliente WHERE id = {id}")
            self.conn.commit()
            print("Cliente deletado com sucesso!!!!")
 
        except Exception as erro:
            print(erro)
 
    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexõs encerrada com sucesso!!!")
 
d1 = Database()
d1.connect()
 
if __name__ == '__main__':
    db = Database()
    # db.connect()
    # db.insert_client()
    # db.select_client()
    db.select_client_by_id(1)
    db.close_connection()
    # db.delete_client(2)
    db.update_client(13)