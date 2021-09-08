# Preparar um relatório que retorne os alunos que passaram direto sem a necessidade da nota do global solution

def relatorio_alunos_passaram_sgs(media_primeiro_semestre, cp_01, cp_02, cp_03, nota_challenge):
    '''
        Essa função deverá retornar um dicionário com os alunos que passaram sem a nota do Global Solution
        Formato do dicionario -> 
        alunos_aprovados = {
            "RM": "nome"
        }

        param1: média do 1º semestre
        param2: nota do Checkpoint 1
        param3: nota do Checkpoint 2
        param4: nota do Checkpoint 3
        param5: nota do challenge

        Regra: A menor nota dos checkpoints é descartada
    '''
    cp_notas = [cp_01, cp_02, cp_03]
    peso_primeiro_semestre = 0.4
    peso_segundo_semestre = 0.6
    menor_nota_cp = min(cp_notas) # Pegando a menor nota
    cp_notas.remove(menor_nota_cp)

    media_cp = sum(cp_notas) / 2


    media_final = media_primeiro_semestre * peso_primeiro_semestre + (((nota_challenge + media_cp) / 2) * 0.4) * peso_segundo_semestre

    # Teste
    return media_final


# Teste
def teste():
    alunos = relatorio_alunos_passaram_sgs(10, 5, 10, 8, 8)
    print(alunos)


teste()

    