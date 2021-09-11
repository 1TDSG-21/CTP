from JoinTech.importDatas import *
from zenGroupModules.relatorio_03 import *
from goCodeFiap.average import *
from Tage.relatorio_01 import *
from TheRevolutionaries.relatorio_02 import *

#By Unknown

lista = getDatas()
nota_gs_min=nota_min_gs(lista) 
aprovado_sem_gs=relatorio_alunos_passaram_sgs(lista)
reprovado_com_gs=relatorio_alunos_nao_passaram(lista)
# print(len(nota_gs_min))
# print(len(lista))
# print(len(aprovado_sem_gs))
# print(len(reprovado_com_gs))
def mostra_info_alunos(lista):
    for i in range(len(lista)):
      print(60*'-')
      print('\t',lista[i]['rm'],'  ',lista[i]['nome'],'\n')
      print("Disciplina:  Computational Thinking using Python")
      print("Semestre 1: {}".format(lista[i]['semestre_01']))
      print("\t\t\tSemestre 2\n")
      print("Checkpoints (média): {:.2f}".format(nota_gs_min[lista[i]['nome']]['ck_media']))
      print("Challenge: {:.2f}".format(nota_gs_min[lista[i]['nome']]['challenge_media']))
      print("Nota mínima na Global Solution para aprovação: {:.2f}".format(nota_gs_min[lista[i]['nome']]['gs_minimo']))
      print(60*'-','\n')
    
# print(mostra_info_alunos(lista))

def mostra_alunos_reprovados():
  if len(reprovado_com_gs)>0:
    print('Alunos que não possuem chance de aprovação na disciplina:\n')
    for rm, nome in reprovado_com_gs.items():
      print('RM: {} - {}'.format(rm,nome))
  else:
    print('Não há alunos reprovados')    

def mostra_alunos_aprovados():
  if len(aprovado_sem_gs)>0:
    print('Alunos já aprovados na disciplina:\n')
    for rm, nome in aprovado_sem_gs.items():
      print('RM: {} - {}'.format(rm,nome))
  else:
    print('Não há alunos aprovados')

print("1) Conforme abaixo, precisa mostrar as informações para todos os alunos cadastrados na planilha:")    
mostra_info_alunos(lista)
print("2) Mostrar a relação dos alunos que não possuem chance de aprovação na disciplina\n")   
mostra_alunos_reprovados()
print("\n3) Mostrar a relação dos alunos que já estão aprovados na disciplina mesmo sem a nota da Global Solution.\n")
mostra_alunos_aprovados()
    