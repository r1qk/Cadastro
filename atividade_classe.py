def menu():
    print("1. Alterar nome\n2. Alterar idade\n3. Alterar endereço\n4. Voltar")
#-------
def mudar_nome(nome_antigo):
    novo_nome = input("Digite o novo nome: ")
    if novo_nome == "":
        print("Este espaço deve ser preenchido\n")
    else:
        print(f"O nome foi alterado de {nome_antigo} para {novo_nome}\n")
        nome_antigo = novo_nome
        
    return nome_antigo    
#------
def mudar_idade (idade_antiga):
    nova_idade = input("Digite a nova idade: ")
    if nova_idade == "":
        print("Este espaço deve ser preenchido\n")
    elif nova_idade.isdigit():
        print(f"A idade foi alterada de {idade_antiga} para {nova_idade}\n")
        idade_antiga = nova_idade
    else:
        print("A idade deve ser um número\n")
        
    return idade_antiga    
#------    
def mudar_endereco (endereco_antigo):
    novo_endereco = input("Digite o novo endereco: ")
    if novo_endereco == "":
        print("Este espaço deve ser preenchido\n")
    else:
        print(f"O endereço foi alterado de {endereco_antigo} para {novo_endereco}\n")
        endereco_antigo = novo_endereco
        
    return endereco_antigo
#------ 
class pessoa:
    def __init__ (self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        
    def __str__ (self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Endereço: {self.endereco}"
while True:
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    endereco = input("Digite seu endereço: ")
    if nome == "" or idade == "" or endereco == "" or (not idade.isdigit()):
        print("Tente novamente\n")
    else:
        idade = int(idade)
        break

p1 = pessoa(nome, idade, endereco)
print("")

while True:
    print(f"Informações digitadas: {p1}")
    mudanca = input("Deseja mudar algo? Digite sim ou não: ")
    if mudanca.lower() == "sim":
        print("")
        menu()
        opcao = int(input("Escolha, com o número, o que quer mudar: "))
        match opcao:
            case 1:
                p1.nome = mudar_nome(p1.nome)
            case 2:
                p1.idade = mudar_idade(p1.idade)
            case 3:
                p1.endereco = mudar_endereco(p1.endereco)
            case 4:
                print("Voltando...\n")
            case _:
                print("Resposta iválida. Tente novamente.\n")
    elif mudanca.lower() == "não" or mudanca.lower() == "nao":
        print("Saindo...")
        break
    else:
        print("Resposta iválida. Tente novamente.\n")
        
print("Fim do programa")
print("Teste para alteração 2")