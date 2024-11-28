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

    def insert_client(self,tupla):
        self.connect()
        try:

            
            self.cursor.execute('INSERT INTO cliente (nome,cpf,login,senha,fone,cidade) VALUES (%s,%s,%s,%s,%s,%s)',tupla)
            self.conn.commit()
            # print("Cliente cadastrado com sucesso!!!")
            return True


        except Exception as err:
            print(err)
        
        finally :
            self.close_connection()


    def insert_product(self):
        self.connect()
        try:
            args = ("Thiago Almeida","555","meulogin","333","222","CG")
            
            self.cursor.execute('INSERT INTO produto (nome,cpf,login,senha,fone,cidade) VALUES (%s,%s,%s,%s,%s,%s)',args)
            self.conn.commit()
            print("Cliente cadastrado com sucesso!!!")

        except Exception as err:
            print(err)
                 
        finally :
            self.close_connection()


    def select_client(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM cliente")
            clientes = self.cursor.fetchall()
            return clientes

        except Exception as err:
            print(err)
                 
        finally :
            self.close_connection()


    def select_client_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cliente WHERE id = {id}")
            cli = self.cursor.fetchone()
            return cli

        except Exception as err:
            print(err)
                 
        finally :
            self.close_connection()


    def update_client(self,dados):
        self.connect()
        try:
         

            self.cursor.execute(f"""
                                UPDATE cliente 
                                SET nome = '{dados[1]}',
                                cpf = '{dados[2]}',
                                login = '{dados[3]}', 
                                senha = '{dados[4]}', 
                                fone = '{dados[5]}',
                                cidade = '{dados[6]}' 
                                WHERE id = {dados[0]} 
                                """)
            self.conn.commit()
            # cli_atualizado = self.select_client_by_id(dados[0])
            # print(cli_atualizado)
            return True
        
        except Exception as erro:
            print(erro)
                 
        finally :
            self.close_connection()


    def delete_client(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cliente WHERE id = {id}")
            self.conn.commit()
            print("CLiente deletado com sucesso!!!")

        except Exception as erro:
            print(erro)     
        finally :
            self.close_connection()

    

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