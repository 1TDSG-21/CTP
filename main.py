from JoinTech.importDatas import *
from zenGroupModules.relatorio_03 import *
from goCodeFiap.average import *
from Tage.relatorio_01 import *
from TheRevolutionaries.relatorio_02 import *
lista = getDatas()
nota_gs_min=nota_min_gs(lista) 
aprovado_sem_gs=relatorio_alunos_passaram_sgs(lista)
reprovado_com_gs=relatorio_alunos_nao_passaram(lista)
print(len(nota_gs_min))
print(len(lista))
print(len(aprovado_sem_gs))
print(aprovado_sem_gs)
def mostra_info_alunos(lista):
	for i in range(len(lista)):
		print(lista[i]['rm'],'  ',lista[i]['nome'])
		print("Disciplina:  Computational Thinking using Python")
		print("Semestre 1: ",lista[i]['semestre_01'])
		print("Semestre 2")
		print("Checkpoints (média): ",nota_gs_min[0][lista[i]['nome']]['ck_media'])
		print("Challenge: ",nota_gs_min[0][lista[i]['nome']]['challenge_media'])
		print("Nota mínima na Global Solution para aprovação: ",nota_gs_min[0][lista[i]['nome']]['gs_minimo'])
# print(lista[0]['rm'])
# print(nota_gs_min[0]['Alfonso Matsuoka Schiavelli'])
# print(mostra_info_alunos(lista))
#print(lista)
# alunos_aprovados_sem_gs = relatorio_alunos_passaram_sgs(lista)
# print(alunos_aprovados_sem_gs)