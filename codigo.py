nome = str(input("nome: "))
turma = str(input("turma: "))
cgm = int(input("cgm: "))

def cadastro_aluno(nome, turma, cgm):
  print("O aluno foi cadastrado!")
  opcao = input("Deseja ver cadastro? Digite 'S' p/ ver: ")
  if opcao == 's' or opcao == 'S':
   print(f"Suas informações são: {nome, turma, cgm}")
  
  else:
    print("Seu cadastro foi concluido")


cadastro_aluno(nome, turma,cgm)
