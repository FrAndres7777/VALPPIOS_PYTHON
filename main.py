import numpy as np

def crear_matriz():
    orden = int(input("Ingrese el orden de la matriz: "))
    matriz = np.zeros((orden, orden))

    for i in range(orden):
        fila = input(f"Ingrese los valores para la fila {i+1} separados por espacios: ")
        valores = fila.split()
        valores_float = []
        for valor in valores:
            valor_float = float(valor)
            valores_float.append(valor_float)
        matriz[i] = valores_float

    return matriz

# Ejemplo de uso
matriz = crear_matriz()
print(matriz,"\n")
listavaloresP=[]
inicio = -100
fin = 100
aumento= 0.10
while inicio <= fin:
    inicio+=aumento
    n = len(matriz[0])
    matrizPrueba = np.zeros((n, n))
    for i in range(0, len(matriz[0])):
        for ii in range(0, len(matriz[0])):
            if ii == i:
                matrizPrueba[ii][i] = matriz[ii][i] -inicio
            else:
                matrizPrueba[ii][i] = matriz[ii][i]
    

    determinante = np.linalg.det(matrizPrueba)
    if determinante ==0:
        print(inicio)
        listavaloresP.append(inicio)
    elif determinante <= 0.01 and determinante >= -00.1:
        print(inicio)
        listavaloresP.append(inicio)
print("valores Propios  : ", listavaloresP)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        