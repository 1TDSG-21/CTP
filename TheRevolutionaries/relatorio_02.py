#Preparar um relatório que retorne os alunos que não possuem chance de aprovação

def relatorio_alunos_nao_passaram(media_primeiro_semestre, cp_01, cp_02, cp_03, nota_challenge_sprint3, nota_challenge_sprint4, nota_global_solution):
    
    '''
        Essa função deverá retornar um dicionário com os alunos que não possuem chance de aprovação (não passarão mesmo que tirem 10 no Global Solution)
        Formato do dicionario -> 
        alunos_nao_aprovados = {
            "RM": "nome"
        }
        param1: média do 1º semestre
        param2: nota do Checkpoint 1
        param3: nota do Checkpoint 2
        param4: nota do Checkpoint 3
        param5: nota do challenge sprint 3
        param6: nota do challenge sprint 4
        param7: nota do Global Solution

        Regra: A menor nota dos checkpoints é descartada
    '''

    cp_notas = [cp_01, cp_02, cp_03]
    peso_primeiro_semestre = 0.4
    peso_segundo_semestre = 0.6
    menor_nota_cp = min(cp_notas) # Pegando a menor nota
    cp_notas.remove(menor_nota_cp)

    media_cp = sum(cp_notas) / 2

    media_challenge = (nota_challenge_sprint3 + nota_challenge_sprint4) / 2
    
    media_cp_challenge = (media_cp + media_challenge)/2

    media_segundo_semestre = (media_cp_challenge * 0.4) + (nota_global_solution * 0.6)

    media_final = (media_primeiro_semestre * peso_primeiro_semestre) + (media_segundo_semestre * peso_segundo_semestre)

    # Teste
    return media_final




#Teste
def teste():
    alunos = relatorio_alunos_nao_passaram(0.5, 0, 0, 0, 0, 0, 10)
    print(alunos)


teste()
