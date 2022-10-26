
global funcionarios
funcionarios = []
def cadastrar_funcionario(*args):

    nome = str(input("Digite o nome do funcionário\n"))
    cpf = int(input("Digite o CPF do funcionário\n"))
    cargo = str(input("Qual o cargo do funcionário?\n"))
    salario = float(input("Informe o salário do funcionário\n"))
    telefones = int(input("Cadastre um telefone para o funcionário\n"))

    funcionario = {
        'nome' : nome.title(),
        'cpf' : cpf,
        'cargo' : cargo,
        'salario' : salario,
        'telefones' : [telefones]    
        }

    funcionarios.append(funcionario)
    print(funcionarios)

def buscar_funcionario(*args):
    if funcionarios == []:
        print('Não há funcionários cadastrados!\n')
    else:
        cpf_busca = int(input("Digite o cpf do funcionário:\n"))
        for consulta in funcionarios:
            if consulta['cpf'] == cpf_busca:
                print(consulta)
                print("Funcionário Cadastrado!")
            else:
                print("Dados Inválido.\nVerifiique se os dados estão corretos!\n")

def apagar_funcionario():
    if funcionarios == []:
        print('Não há funcionários cadastrados!\n')
    else:
        cpf_busca = int(input("Digite o cpf do funcionário:\n"))
        for consulta in funcionarios:
            if consulta['cpf'] == cpf_busca:
                print(consulta)
                print("Funcionário Cadastrado!")
                funcionarios.remove(consulta)
                print(funcionarios)
                print("Conta apagada!")
            else:
                print("Dados Inválido.\nVerifiique se os dados estão corretos!\n")

def editar_dados():
    if funcionarios == []:
        print('Não há funcionários cadastrados!\n')
    else:
        cpf_busca = int(input("Digite o cpf do funcionário:\n"))
        for busca in funcionarios:
            if busca['cpf'] == cpf_busca:
                nome = str(input("Digite o nome do funcionário\n"))
                cpf = int(input("Digite o CPF do funcionário\n"))
                cargo = str(input("Qual o cargo do funcionário?\n"))
                salario = float(input("Informe o salário do funcionário\n"))
                telefones = int(input("Cadastre um telefone para o funcionário\n"))
                busca['nome'] = nome.title()
                busca['cpf'] = cpf
                busca['cargo'] = cargo
                busca['salario'] = salario
                busca['telefones'] = telefones
                print(funcionarios)
            else:
                print("Dados iválidos.\nverfique se os dados estão corretos!\n")

def novo_telefone():
    if funcionarios == []:
        print('Não há funcionários cadastrados!\n')
    else:
        cpf_busca = int(input("Digite o cpf do funcionário:\n"))
        for busca in funcionarios:
            if busca['cpf'] == cpf_busca:
                novo_telefone = int(input("Cadastre um telefone para o funcionário\n"))
                busca['telefones'].append(novo_telefone)
                print(funcionarios)
            else:
                print("Dados iválidos.\nverfique se os dados estão corretos!\n")


def menu():
    menu = True
    while menu:
        print("""
        1 - Cadastro de Funcionários
        2 - Pesquisar Funcionário
        3 - Cadastrar novo Telefone
        4 - Editar dados do Funcionário
        5 - Deletar Funcionário
        0 - Sair
        """)
        op = int(input("Entre com uma opção do Menu\n"))
        if op == 1:
            cadastrar_funcionario()
        elif op == 2:
            buscar_funcionario()
        elif op == 3:
            novo_telefone()
        elif op == 4:
            editar_dados()
        elif op == 5:
            apagar_funcionario()
        elif op == 0:
            break


menu()
