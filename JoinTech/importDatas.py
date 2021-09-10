import pandas as pd

def getDatas():
    fileCsv = pd.read_csv("JoinTech/notas_planilha_modelo2.csv" , sep=';')
    lista = []
    for i,item in enumerate(fileCsv.values):
        if i >= 2:
            lista.append({
                'rm': item[0],
                'nome': item[1],
                'semestre1' : item[2],
                'semestre2' : {
                'checkpoint_01' : item[4],
                'checkpoint_02' : item[5],
                'checkpoint_03' : item[6],
                'challenge_03' : item[8],
                'challenge_04' : item[9]

                }

            })
    return lista 

