
# para usar nossa funcao precisa do modelo de lista abaixo
# gabriel = [["Semestre_1","6"],["Semestre_2","checkpoint1","8","checkpoint2",
#    "7","checkpoint3","8","Challenge Sprint 3", "3,0","Challenge Sprint 4", "3,0",
# ]]
# nos usmamos o tutorial abaixo para criar uma lista de dados atraves do 
# excel
# https://www.delftstack.com/pt/howto/python/how-to-read-csv-to-list-in-python/
# os dados estao na planinha modelo que esta em pdf
# a validacao das notas maiores ja foi criado entao nao precisa se preocupar
# a tabela acima e ficticia,voce precisa criar os alunos com os dados correspondente


def handleCalculation(secondSemester):
    sumCheckpoint = 0
    if(float(secondSemester[2]) > float(secondSemester[4]) and float(secondSemester[2]) > float(secondSemester[6])  ):
          if((secondSemester[4]) > float(secondSemester[6])):
            sumCheckpoint =  float(secondSemester[2]) + float(secondSemester[4])
            return sumCheckpoint
          else:
              sumCheckpoint =  float(secondSemester[2]) + float(secondSemester[6])
              return sumCheckpoint
    elif(float(secondSemester[4]) > float(secondSemester[6]) and float(secondSemester[4]) > float(secondSemester[2]) ):
          if(float(secondSemester[2]) > float(secondSemester[6])):
            sumCheckpoint =  float(secondSemester[4]) + float(secondSemester[2])
            return sumCheckpoint
          else:
              sumCheckpoint =  float(secondSemester[4]) + float(secondSemester[6])
              return sumCheckpoint
    elif(float(secondSemester[2]) > float(secondSemester[4])):
            sumCheckpoint =  float(secondSemester[6]) + float(secondSemester[2]) 
            return sumCheckpoint
    else:
            sumCheckpoint =  float(secondSemester[6]) + float(secondSemester[4]) 
            return sumCheckpoint
def handleAverage(user):
    firstSemester=   user[0] 
    secondSemester = user[1]
    resultsSumCheckpoint = handleCalculation(secondSemester) / 2.0
    firstSprintFormated =  secondSemester[8].split(",")
    secondSprintFormated = secondSemester[10].split(",")
    resultsSumSprint = (float(firstSprintFormated[0]) + float(secondSprintFormated[0]))/2
    totalSecondSemester = (resultsSumCheckpoint + resultsSumSprint ) * 0.4
    averageYear = (totalSecondSemester * 0.6) + (float(firstSemester[1])*0.4)
    # print(resultsSumCheckpoint, "EU SOU TOTAL DA MEDIA DOS CHECkPOINT")
    # print(resultsSumSprint, "EU SOU TOTAL DA MEDIA DOS SPRINT")
    # print(totalSecondSemester,"EU SOU TOTAL DO SEGUNDO SEMESTRE")
    # print(float(firstSemester[1]),"EU SOU TOTAL DO PRIMEIRO SEMESTRE")
    # # print(averageYear)
    return  averageYear

# repare que a funcao precisa de um parametro
handleAverage(parametro) 
# todo comentairo e com intencao de auxiliar no uso da funcao
# ela vai retornar o calculo anual. Usamos a formula modelo 
# Ma= (0.4*primerio semestre) + (0.6*segundo semestre)
# A funcao precisa da lista acima, 
# exemplo de uso da funcao
# total = handleAverage(gabriel)
# print (total)
# a funcao vai retornar a media anual de acordo com os dados do aluno inserido
# a formula para calcular media dos checkpoint foi a soma das duas maiores e 
# dividiu por dois
# mesmo e valido para formula dos sprint





