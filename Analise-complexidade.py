import random
import time

# Algoritmo 1: Complexidade O(n^2)
def algoritmo1(n):
    soma = 0
    for i in range(n):
        for j in range(n):
            aleatorio = random.randint(1, 1000)
            soma += aleatorio

    return soma

# Algoritmo 2: Complexidade O(n^3)
def algoritmo2(n):
    soma = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                aleatorio = random.randint(1, 1000)
                soma += aleatorio

    return soma

# Medição de tempo para cada valor de n
valores_n = [10, 100, 1000]

for n in valores_n:
    start_time = time.time()
    resultado_algoritmo1 = algoritmo1(n)
    end_time = time.time()
    tempo_execucao_algoritmo1 = end_time - start_time

    start_time = time.time()
    resultado_algoritmo2 = algoritmo2(n)
    end_time = time.time()
    tempo_execucao_algoritmo2 = end_time - start_time

    print(f"Valor de n: {n}")
    print(f"Tempo de execução do Algoritmo 1: {tempo_execucao_algoritmo1} segundos")
    print(f"Tempo de execução do Algoritmo 2: {tempo_execucao_algoritmo2} segundos")
    print()
