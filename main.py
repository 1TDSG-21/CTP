from JoinTech.importDatas import *
from zenGroupModules.relatorio_03 import *
lista = getDatas()

#print(lista)
alunos_aprovados_sem_gs = relatorio_alunos_passaram_sgs(lista)
print(alunos_aprovados_sem_gs)