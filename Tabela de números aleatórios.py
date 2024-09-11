#AMOSTRAGEM - TABELA DE NÚMEROS ALEATÓRIOS
import numpy as np

size = 3;

def matrizCreate (size):
    popMatriz = np.zeros((size,size))
    for i in range(0,size,1):
        for j in range(0,size,1):
            popMatriz[i,j]=np.random.randint(1,50);
    return popMatriz

matrizCreate(size)
print(matrizCreate(size))
