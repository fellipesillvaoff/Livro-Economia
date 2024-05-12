import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do modelo
alpha = 0.55  # participação do capital físico
beta = 0.45   # participação da mão de obra considerar beta (1-alpha) quando necessário
s = 0.30      # taxa de poupança
delta = 0.05 # taxa de depreciação do capital físico
n = 0.01     # taxa de crescimento populacional
g = 0.03     # taxa de crescimento tecnológico
K=1000000       #Capital inicial no T=0
L=10      #trabalhodores no T=0
T=150 #numero de periodos
# Nomear as colunas da matriz
column_names = ['Capital Físico (K)', 'Produto Total (Y)', 'Poupança', 'Depreciação']

# Inicializar matriz para armazenar valores
K_values = np.zeros((T, 4), dtype=object)  # 101 linhas para os períodos de tempo de 0 a 100, 4 colunas para as variáveis

# Atribuir nomes às colunas
K_values[0] = column_names

# Função de produção
def production_function(K, H, L):
    return (K ** alpha) * (H ** (1 - alpha)) * (L ** beta)

# Valores para o capital físico (K) e a força de trabalho (L)
for i in range(T):
    K = i
    Y = production_function(K, 1, L)
    savings = s * Y
    depreciation = (delta + n + g) * K
    K_values[i] = [K, Y, savings, depreciation]

    

# Encontrar a interseção entre a poupança e a depreciação
intersection_index = np.argmin(np.abs(K_values[:, 2] -  K_values[:, 3]))+1

import numpy as np



# Vamos supor que queremos calcular a diferença entre a primeira e a segunda coluna
coluna1 = K_values[:, 2]
coluna2 = K_values[:, 3]

# Inicialize variáveis para armazenar a posição e o valor mais próximo de zero
posicao_mais_proxima = None
valor_mais_proximo = np.inf

# Itere sobre os índices da matriz
for i in range(1,len(coluna1)):
    # Calcule a diferença entre os elementos das duas colunas
    diferenca = coluna1[i] - coluna2[i]
    
    # Verifique se a diferença é mais próxima de zero do que o valor atual
    if abs(diferenca) < abs(valor_mais_proximo):
        valor_mais_proximo = diferenca
        intersection_index = i

# Exiba o resultado
print("Posição mais próxima de zero:", posicao_mais_proxima)
print("Diferença mais próxima de zero:", valor_mais_proximo)


# Plotar os resultados
plt.figure(figsize=(10, 6))

plt.plot(K_values[:, 0], K_values[:, 1], label='Produto Total (Y)', color='blue')  # Produto Total (Y) em relação ao tempo
plt.plot(K_values[:, 0], K_values[:, 2], label='Poupança', color='green')          # Poupança em relação ao tempo
plt.plot(K_values[:, 0], K_values[:, 3], label='Depreciação', color='red')         # Depreciação em relação ao tempo

# Adicionar ponto de interseção
plt.scatter(K_values[intersection_index, 0], K_values[intersection_index, 2], color='black', marker='o', label=f'Interseção Periodo:{intersection_index}')

# Adicionar linhas verticais para destacar os períodos de tempo
plt.axvline(x=K_values[intersection_index, 0], linestyle='--', color='gray', )
#plt.axvline(x=K_values[intersection_index, 2], linestyle='--', color='orange', label='Tempo 100')

# Adicionar linhas horizontais para destacar os valores de Y
plt.axhline(y=K_values[intersection_index, 1], linestyle='--', color='gray', label=f'Y Comsumo=y-(S*F(K)) R${int((K_values[intersection_index,1]-K_values[intersection_index,2])*1000)} Bi')
#plt.axhline(y=K_values[intersection_index+10, 1], linestyle='--', color='orange', label=f'Y Tempo {intersection_index}: {K_values[-1, 1]:.2f}')

plt.xlabel('Tempo')
plt.ylabel('Valores')
plt.title('Função de Produção, Poupança e Depreciação ao Longo do Tempo')
plt.legend()
plt.grid(True)
plt.show()
