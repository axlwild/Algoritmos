"""
class collections.Counter([iterable-or-mapping])
similar a multiset
UVa 987
Entradas:
	N:	número de casos de prueba
	B:	campos de batalla.
	SG:		lemmings verdes
	SB:		lemmings azules


Como se tienen que ordenar por poder, se opta por utilizar lista.


mientras haya vivos en los dos equipos.
	Se reparten los mejores en los B campos como máximo. **
		-Se debe de considerar que puede haber menos de B lemmings en cada equipo.
		-Se debe de considerar que se deben de mandar la misma cantidad de lemmings de
			cada equipo a la batalla.

	Batallan:
		Se determina quiénes murieron.
		Se actualizan lemmings vivos con su respectivo poder.
		Se actualiza orden de poder.

mostrar ganadores.

"""
N=int(input())
for prueba in range(N):
	B,SG,SB = [int(x) for x in input().split()]
	azules = []
	verdes = []
	for i in range(SG):
		verdes.append(int(input()))
	for j in range(SB):
		azules.append(int(input()))
	while len(azules) > 0 < len(verdes):
		azules.sort(reverse=True)
		verdes.sort(reverse=True)
		muertesAzul=0
		muertesVerde=0
		for i in range(B):
			#Si hay menos lemmings que campos de cualquier equipo, hasta ahí se batalla.
			#if i > len(verdes)
			#Solo se puede entra hasta el len(a)-1
			#entonce se tiene que cumplir que i <= len(a) - 1
			#entonces no puede ser que i > len(a) -1
			# 						    i + 1 > len(a)
			# alv sea el señor no sale
			if (len(verdes) < i+1) or (len(azules)< i+1): 
				break
			"""
			print(i)
			print(len(verdes))
			print(len(azules))
			print()
			"""
			peleadores=azules[i]-verdes[i]
			#Gana azul, muere verde
			if peleadores > 0:
				azules[i],verdes[i] = peleadores,0
				muertesVerde+=1
			#Gana verde, muere azul
			elif peleadores < 0:
				verdes[i],azules[i] = peleadores*-1,0
				muertesAzul+=1
			#Todos mueren.
			else:
				azules[i],verdes[i]=0,0
				muertesAzul += 1
				muertesVerde += 1
		#Aquí quitamos a los muertos
		for i in range(muertesAzul):
			azules.remove(0)
		for i in range(muertesVerde):
			verdes.remove(0)
	azules.sort(reverse=True)
	verdes.sort(reverse=True)
	if len(azules) > 0:
		print("blue wins")
		for i in azules:
			print(i)
	elif len(verdes) > 0:
		print("green wins")
		for i in verdes:
			print(i)
	else:
		print("green and blue died")
		
	if prueba!=N-1:
		print()

