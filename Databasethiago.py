import mysql.connector

class Database():
    def __init__(self, banco="syspython"):
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='localhost',database=self.banco,user='root',password='')

        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado com sucesso: ",db_info)
        else:
            print("ERROR")

    def insert_client(self):
        self.connect()
        try:
            args = ("Thiago Almeida","55","meulogin","333","222","CG")
            
            self.cursor.execute('INSERT INTO cliente (nome,cpf,login,senha,fone,cidade) VALUES (%s,%s,%s,%s,%s,%s)',args)
            self.conn.commit()
            print("Cliente cadastrado com sucesso!!!")

        except Exception as err:
            print(err)

    def insert_product(self):
        self.connect()
        try:
            args = ("Thiago Almeida","555","meulogin","333","222","CG")
            
            self.cursor.execute('INSERT INTO produto (nome,cpf,login,senha,fone,cidade) VALUES (%s,%s,%s,%s,%s,%s)',args)
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
                print(cli)

        except Exception as err:
            print(err)

    def select_client_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cliente WHERE id = {id}")
            cli = self.cursor.fetchone()
            return cli

        except Exception as err:
            print(err)

    def update_client(self,id):
        self.connect()
        try:
            cliente = list(self.select_client_by_id(id))
            print(cliente)
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
            print(cli_atualizado)
        
        except Exception as erro:
            print(erro)

    def delete_client(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cliente WHERE id = {id}")
            self.conn.commit()
            print("CLiente deletado com sucesso!!!")

        except Exception as erro:
            print(erro)
    

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada com sucesso!!")


if __name__ == '__main__':
    db = Database()
    db.connect()
    db.insert_client()
    #db.update_client(6)
    #db.delete_client(8)
    #db.close_connection()