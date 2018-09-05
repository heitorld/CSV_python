import csv
import time
partidos = {}
with open("eleicao.csv", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=';')

    for n, row in enumerate(reader):
        if not n:
            # Skip header row (n = 0).
            continue  
    
        numero, nome, partido, votos = row
    
        if partido not in partidos:
            partidos[partido] = list()
    
        partidos[partido].append((numero, nome, int(votos)))
# Dicionario para armazenar a quantidade total de votos por partido e a quantidade de candidatos por partido
votosPartidos = {}
# Percorrer cada chave do dicionario partidos e ordenar de forma decrescente os votos
from operator import itemgetter
votosPorPartido = int(0)
totalVotos = int(0)
for partidosKey in partidos.keys():
	subList = partidos.get(partidosKey)
	subList.sort(key=itemgetter(2), reverse=True)	
	
	for x, y, z in subList:
		votosPorPartido = z + votosPorPartido
		totalVotos = z + totalVotos
	votosPartidos[partidosKey]= list()
	votosPartidos[partidosKey].append((int(votosPorPartido)))
	votosPorPartido = 0


print("Dicionario com a quantidade de votos ordenada de forma decrescente")
print(partidos)
#time.sleep(5)

print("Dicionario com a quantidade total de votos por partido")
print(votosPartidos)

print("Total de votos: " + str(totalVotos))

qE = int(totalVotos / 30)
print("Quociente eleitoral: " + str(qE))

totalQP = 0
QP = {}
for x in votosPartidos.keys():
	subList = votosPartidos.get(x)
	#print(subList)
	for y in subList:
		qP = int(y / qE)
		totalQP = totalQP + qP
	QP[x] = int(qP)
	qP = 0

print("Total QP: " + str(totalQP))
print(QP)



###SUPONDO QUE NAO TENHA VAGA RESIDUAL, OS CANDIDATOS ELEITOS SERIAM:
out = open("eleicao.tsv", "x") 
it = int(0)
for a in QP:
	it = int(QP[a])
	#print(it)
	i=0
	while(it > 0):
		
		it = it -1
		out.write(str(a) + "  "+ str(partidos[a][i]))
		print(str(a) + "  "+ str(partidos[a][i]))
		
		i=i+1


#if (totalQP < 30):
#vagasResiduais = 30 - totalQP

#for (k,v), (k2,v2) in zip(QP.items(), votosPartidos.items()):
#	print(k, v)
#	print(k2, v2)
#	time.sleep(1)
