def nota_min_gs(lista):

    aluno = dict()

    for i in lista:
        cp_notas = [float(i["semestre_02"]["checkpoint_01"]), float(i["semestre_02"]["checkpoint_02"]), float(i["semestre_02"]["checkpoint_03"])]
        peso_primeiro_semestre = 0.4
        peso_segundo_semestre = 0.6
        menor_nota_cp = min(cp_notas) # Pegando a menor nota
        cp_notas.remove(menor_nota_cp)
        media_cp = sum(cp_notas) / 2
        media_challenge = (float(i["semestre_02"]["challenge_03"]) + float(i["semestre_02"]["challenge_04"])) / 2

        media_final = float(i["semestre_01"]) * peso_primeiro_semestre + (((media_challenge + media_cp) / 2) * 0.4) * peso_segundo_semestre
        sobra = 6 - media_final

        if sobra > 0:
            gs_min = (sobra * 10) / 6

        elif media_final < 6:
            aluno[i["nome"]] = dict(rm=i["rm"],sem1=i["semestre_01"] , ck_media=media_cp, challenge_media=media_challenge, gs_minimo=round(gs_min, 2))
        elif media_final > 6:
               aluno[i["nome"]] = dict(rm=i["rm"],sem1=i["semestre_01"], ck_media=media_cp, challenge_media=media_challenge, gs_minimo=0)
        else:
            print("notas invalida")
    
    return aluno





