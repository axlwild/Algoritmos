import numpy as np

def sumaTodos(numero,arr):
#Primero solo hay una bifurcacion
	if len(arr)==1:
		return
	arr=np.sort(arr)

	if np.array2string(arr) in dic:
		return
	else:
		dic[np.array2string(arr)]=arr
		#se elimina un elemento del arreglo
		arraux=np.copy(arr)
		print(arraux)
		
		arraux[-2]=arraux[-1]+arraux[-2]
		#if len(arraux)<=2:
		#	return
		#Primer caso: sumar los últimos dos, quedando uno menos

		sumaTodos(numero,arraux[:-1])
		arraux=np.copy(arr)
		arraux[1]=arraux[1]+arraux[0]
		sumaTodos(numero,arraux[1:])
		#Sumar cada uno con el resto del arreglo
		
		


def prueba(numero):
	global a
	global dic
	dic={}
	arr=np.ones([numero])
	sumaTodos(numero,arr)

	
a=np.ones([])
dic={}


a=input("número a descomponer: ")
prueba(int(a))
print(len(dic))



