trabalho Academia
class Aluno:
 def __init__(self, nome, cpf, peso, altura):
 self.nome = nome
 self.cpf = cpf
 self.peso = peso
 self.altura = altura
 self.status = False
 # A classe Aluno define a estrutura de um aluno, com atributos como 
nome, CPF, peso, altura e status (que indica se o aluno está ativo ou inativo).
class Exercicio:
 def __init__(self, nome, repeticoes, peso):
 self.nome = nome
 self.repeticoes = repeticoes
 self.peso = peso
# A classe Exercicio define a estrutura de um exercício, com atributos como 
nome, número de repetições e peso.
class Academia:
 def __init__(self):
 self.alunos = []
 self.treinos = []
 # A classe Academia representa a academia em si. Ela possui uma lista 
de alunos e uma lista de treinos correspondentes aos alunos.
 def cadastrar_aluno(self, nome, cpf, peso, altura):
 aluno = Aluno(nome, cpf, peso, altura)
 self.alunos.append(aluno)
 self.treinos.append([]) # Cada aluno tem um treino correspondente
 # O método cadastrar_aluno cria um objeto Aluno com as informações 
fornecidas e o adiciona à lista de alunos. Também é adicionada uma lista
vazia na lista de treinos para o aluno recém-cadastrado.
 def buscar_aluno(self, nome):
 for aluno in self.alunos:
 if aluno.nome == nome:
 return aluno
 return None
 # O método buscar_aluno percorre a lista de alunos e retorna o objeto 
Aluno correspondente ao nome fornecido. Caso não encontre o aluno, 
retorna None
 def atualizar_cadastro(self, nome, cpf, peso, altura):
 aluno = self.buscar_aluno(nome)
 if aluno:
 aluno.cpf = cpf
 aluno.peso = peso
 aluno.altura = altura
 print("Cadastro atualizado com sucesso.")
 else:
 print("Aluno(a) não encontrado.")
 # O método atualizar_cadastro busca o aluno com o nome fornecido 
e atualiza as informações de CPF, peso e altura. Se o aluno for encontrado, 
imprime uma mensagem de sucesso. Caso contrário, exibe uma mensagem 
de aluno não encontrado.
 def excluir_aluno(self, nome):
 aluno = self.buscar_aluno(nome)
 if aluno:
 self.alunos.remove(aluno)
 index = self.alunos.index(aluno)
 self.treinos.pop(index)
 print("Aluno(a) removido com sucesso.")
 else:
 print("Aluno(a) não encontrado.")
 # O método excluir_aluno busca o aluno com o nome fornecido e o 
remove da lista de alunos. Além disso, remove o treino correspondente 
usando o índice obtido pela função index. Se o aluno for encontrado, imprime 
uma mensagem de sucesso. Caso contrário, exibe uma mensagem de aluno 
não encontrado.
 def gerenciar_treino(self, nome):
 aluno = self.buscar_aluno(nome)
 if aluno:
 treino = self.treinos[self.alunos.index(aluno)]
 print(f"Treino do aluno(a) {aluno.nome}:")
 self.exibir_treino(treino)
 opcao = input(
 "Escolha uma opção:\n"
 "1 - Incluir novo exercício\n"
 "2 - Alterar exercício existente\n"
 "3 - Excluir exercício\n"
 "4 - Excluir todos os exercícios\n"
 "0 - Voltar\n"
 "Opção: "
 )
 if opcao == "1":
 self.incluir_exercicio(treino)
 aluno.status = True
 elif opcao == "2":
 self.alterar_exercicio(treino)
 elif opcao == "3":
 self.excluir_exercicio(treino)
 if len(treino) == 0:
 aluno.status = False
 elif opcao == "4":
 self.excluir_todos_exercicios(treino)
 aluno.status = False
 elif opcao == "0":
 return
 else:
 print("Opção inválida.")
 # O método gerenciar_treino busca o aluno com o nome fornecido 
e obtém o treino correspondente na lista de treinos. O treino será usado para 
realizar operações como inclusão, alteração e exclusão de exercícios.
 def incluir_exercicio(self, treino):
 nome_exercicio = input("Nome do exercício: ")
 repeticoes = int(input("Número de repetições: "))
 peso = float(input("Peso utilizado: "))
 exercicio = Exercicio(nome_exercicio, repeticoes, peso)
 if exercicio in treino:
 print("O exercício já existe no treino.")
 else:
 treino.append(exercicio)
 print("Exercício incluído no treino.")
 # O método incluir_exercicio solicita ao usuário as informações do 
novo exercício e cria um objeto Exercicio com essas informações. Se o 
exercício já existir no treino, exibe uma mensagem informando. Caso 
contrário, adiciona o exercício ao treino.
 def alterar_exercicio(self, treino):
 nome_exercicio = input("Nome do exercício a ser alterado: ")
 for exercicio in treino:
 if exercicio.nome == nome_exercicio:
 repeticoes = int(input("Novo número de repetições: "))
 peso = float(input("Novo peso utilizado: "))
 exercicio.repeticoes = repeticoes
 exercicio.peso = peso
 print("Exercício alterado com sucesso.")
 return
 print("Exercício não encontrado.")
 # O método alterar_exercicio solicita ao usuário o nome do exercício a ser 
alterado. Em seguida, percorre o treino em busca do exercício com o nome 
fornecido. Se o exercício for encontrado, solicita as novas informações de 
repetições e peso e atualiza o exercício. Caso contrário, exibe uma 
mensagem informando que o exercício não foi encontrado.
 def excluir_exercicio(self, treino):
 nome_exercicio = input("Nome do exercício a ser excluído: ")
 for exercicio in treino:
 if exercicio.nome == nome_exercicio:
 treino.remove(exercicio)
 print("Exercício excluído do treino.")
 return
 print("Exercício não encontrado.")
 # O método excluir_exercicio solicita ao usuário o nome do exercício a 
ser excluído. Em seguida, percorre o treino em busca do exercício com o 
nome fornecido. Se o exercício for encontrado, remove-o do treino. Caso 
contrário, exibe uma mensagem informando que o exercício não foi 
encontrado
 def excluir_todos_exercicios(self, treino):
 treino.clear()
 print("Todos os exercícios foram excluídos do treino.")
 # O método excluir_todos_exercicios remove todos os exercícios do 
treino, deixando-o vazio.
 def exibir_treino(self, treino):
 if len(treino) > 0:
 print("Exercícios:")
 for exercicio in treino:
 print(
 f"- Nome: {exercicio.nome}, Repetições: {exercicio.repeticoes}, 
Peso: {exercicio.peso}"
 )
 else:
 print("O treino está vazio.")
 # O método exibir_treino exibe os exercícios presentes no treino. Se 
o treino estiver vazio, exibe uma mensagem informando que o treino está 
vazio.
 def consultar_aluno(self, nome):
 aluno = self.buscar_aluno(nome)
 if aluno:
 print(f"Nome: {aluno.nome}")
 print(f"CPF: {aluno.cpf}")
 print(f"Peso: {aluno.peso}")
 print(f"Altura: {aluno.altura}")
 print("Treino:")
 self.exibir_treino(self.treinos[self.alunos.index(aluno)])
 else:
 print("Aluno(a) não encontrado.")
 # O método consultar_aluno busca o aluno com o nome fornecido e 
exibe as informações do aluno, incluindo seu treino.
 def relatorio_alunos(self, status):
 if status == "ativos":
 alunos = [aluno for aluno in self.alunos if aluno.status]
 elif status == "inativos":
 alunos = [aluno for aluno in self.alunos if not aluno.status]
 else:
 alunos = self.alunos
 alunos_ordenados = sorted(alunos, key=lambda x: x.nome)
 for aluno in alunos_ordenados:
 print(
 f"Nome: {aluno.nome}, CPF: {aluno.cpf}, Status: {'Ativo' if 
aluno.status else 'Inativo'}"
 )
# O método relatorio_alunos exibe um relatório dos alunos com base no 
status fornecido. Se o status for "ativos", exibe apenas os alunos ativos. Se o 
status for "inativos", exibe apenas os alunos inativos. Caso contrário, exibe 
todos os alunos. Os alunos são ordenados pelo nome antes de serem 
exibidos.
# No restante do código, é criada uma instância da classe Academia e é 
exibido um menu para que o usuário possa interagir com as opções 
disponíveis. Cada opção do menu chama um método correspondente da 
classe Academia para realizar as operações desejadas.
academia = Academia()
while True:
 print("\nMenu principal:")
 print("1 - Cadastrar aluno")
 print("2 - Gerenciar treino")
 print("3 - Consultar aluno")
 print("4 - Atualizar cadastro do aluno")
 print("5 - Excluir aluno")
 print("6 - Relatório de alunos")
 print("0 - Sair")
 opcao_menu = input("Opção: ")
 if opcao_menu == "1":
 nome = input("Nome: ")
 cpf = input("CPF: ")
 peso = float(input("Peso: "))
 altura = float(input("Altura: "))
 academia.cadastrar_aluno(nome, cpf, peso, altura)
 print("Aluno(a) cadastrado com sucesso.")
 elif opcao_menu == "2":
 nome = input("Nome do aluno(a): ")
 academia.gerenciar_treino(nome)
 elif opcao_menu == "3":
 nome = input("Nome do aluno(a): ")
 academia.consultar_aluno(nome)
 elif opcao_menu == "4":
 nome = input("Nome do aluno(a): ")
 cpf = input("Novo CPF: ")
 peso = float(input("Novo peso: "))
 altura = float(input("Nova altura: "))
 academia.atualizar_cadastro(nome, cpf, peso, altura)
 elif opcao_menu == "5":
 nome = input("Nome do aluno(a): ")
 academia.excluir_aluno(nome)
 elif opcao_menu == "6":
 print("Opções de relatório:")
 print("1 - Todos os alunos(a)")
 print("2 - Alunos(a) ativos")
 print("3 - Alunos(a) inativos")
 opcao_relatorio = input("Opção: ")
 if opcao_relatorio == "1":
 academia.relatorio_alunos("todos")
 elif opcao_relatorio == "2":
 academia.relatorio_alunos("ativos")
 elif opcao_relatorio == "3":
 academia.relatorio_alunos("inativos")
 else:
 print("Opção inválida.")
 elif opcao_menu == "0":
 print("Até mais")
 break
 else:
 print("Opção inválida."S