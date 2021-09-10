# Preparar um relatório que retorne os alunos que passaram direto sem a necessidade da nota do global solution

def relatorio_alunos_passaram_sgs(alunos_data):
    '''
        Essa função deverá retornar um dicionário com os alunos que passaram sem a nota do Global Solution
        Formato do dicionario -> 
        alunos_aprovados = {
            "RM": "nome"
        }

        param1: Lista com os dados de todos os alunos

        Regra: A menor nota dos checkpoints é descartada
    '''
    alunos_aprovados_sem_gs = dict()

    for i in alunos_data:
        cp_notas = [i["checkpoint_01"], i["checkpoint_02"], i["checkpoint_01"]]
        peso_primeiro_semestre = 0.4
        peso_segundo_semestre = 0.6
        menor_nota_cp = min(cp_notas) # Pegando a menor nota
        cp_notas.remove(menor_nota_cp)
        media_cp = sum(cp_notas) / 2
        media_challenge = (i["challenge_03"] + i["challenge_04"]) / 2

        media_final = i["semestre_01"] * peso_primeiro_semestre + (((media_challenge + media_cp) / 2) * 0.4) * peso_segundo_semestre

        # Condição para salvar o aluno na lista
        if media_final >= 6.0:
            alunos_aprovados_sem_gs[i["rm"]] = i["nome"]


    return alunos_aprovados_sem_gs


# Teste
def teste():
    ...


teste()

    