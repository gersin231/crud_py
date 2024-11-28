from Entity.Cliente import Cliente

cli1= Cliente()

clientes=cli1.selecionar()
for cliente in clientes:
    print(cliente)

    print("\n SELECIONE UM CLIENTE PARA EDITAR!")

    id_selecao = int(input("DIGITE o ID: "))

    cli_selecionado =list(cli1.selecionar_por_id(id_selecao))


cli_selecionado[1] = input("Digite o novo NOME: ")
cli_selecionado[2] = input("Digite o novo CPF: ")
cli_selecionado[3] = input("Digite o novo LOGIN: ")
cli_selecionado[4] = input("Digite o novo SENHA: ")
cli_selecionado[5] = input("Digite o novo FONE: ")
cli_selecionado[6] = input("Digite o novo CIDADE: ")

atualiza = cli1.atualizar(cli_selecionado)
if atualiza:
    print("\n Cliente Atualizado com SUCESSO")

# cli1.nome = input("Digite Seu Nome: ")
# cli1.cpf = input("Digite Seu Nome: ")
# cli1.login = input("Digite Seu Nome: ")
# cli1.senha = input("Digite Seu Nome: ")
# cli1.fone = input("Digite Seu Nome: ")
# cli1.cidade = input("Digite Seu Nome: ")
# cadastro=cli1.cadastrar()

# print("\n DESEJA DELETAR ALGUEM")
# id_deletar = input(int("DIGITE O ID DO CABOCLO: "))
# cli_deletado = cli1.deletar(id_deletar)

# if cli_deletado == True:
#     print

# # banco= Database()

# # banco.select_client()

# # dados= banco.select_client()

# # print(type(dados))
# # print("Clientes Cadastrados: ")

# # for item in dados:
# #     print(item)

# #     print("\n SELECIONE UM CLIENTE PARA EDITAR!")

# #     id_selecao = int(input("DIGITE o ID: "))

# #     cli_selecionado =list(banco.select_client_by_id(id_selecao))


# # cli_selecionado[1] = input("Digite o novo NOME: ")
# # cli_selecionado[2] = input("Digite o novo CPF: ")
# # cli_selecionado[3] = input("Digite o novo LOGIN: ")
# # cli_selecionado[4] = input("Digite o novo SENHA: ")
# # cli_selecionado[5] = input("Digite o novo FONE: ")
# # cli_selecionado[6] = input("Digite o novo CIDADE: ")

# # atualiza = banco.update_client(cli_selecionado)
# # if atualiza:
# #     print("\n Cliente Atualizado com SUCESSO")