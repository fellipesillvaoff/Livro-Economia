import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x_itens=2
X_Cesta_de_consumo =np.zeros((x_itens, 2), dtype=object)
P_Preços =np.zeros((x_itens, 2), dtype=object)
B_Cestas_Fativel=None
W_renda=51
W_renda2=55
LimiteY=None
LimiteX=None

X_Cesta_de_consumo[0, 0] = 2  #quant do x1
X_Cesta_de_consumo[1, 0] = 5  #preço do x2
P_Preços[0, 0] = 2  # Índice corrigido de [1, 1] para [0, 0]
P_Preços[1, 0] = 5 

X_Cesta_de_consumo[0, 1] = 2.2  #quant do x1
X_Cesta_de_consumo[1, 1] = 5.5  #preço do x2
P_Preços[0, 1] = 3  # Índice corrigido de [1, 1] para [0, 0]
P_Preços[1, 1] = 3 

def orçamento_factivel(t):
        B_Cestas_Fativel=None
        for i in range(t):
                B_Cestas_Fativel=+X_Cesta_de_consumo[t,1]*P_Preços[t,1]
        return B_Cestas_Fativel

print(X_Cesta_de_consumo,P_Preços,B_Cestas_Fativel)

# Calcular os limites do eixo y (quantidade do segundo item) e do eixo x (quantidade do primeiro item)


# Plotar os resultados
plt.figure(figsize=(10, 6))

plt.plot([0, W_renda / P_Preços[0, 0]], [ W_renda / P_Preços[1, 0], 0], label='Orçamento competitivo', color='blue')  # Linha que conecta os limites
plt.fill_between([0, W_renda / P_Preços[0, 0]], [W_renda / P_Preços[1, 0], 0], color='blue', alpha=0.3)  # Colorindo a área abaixo da linha de renda
plt.plot([0,  W_renda2 / (P_Preços[0, 0]*1.10)], [W_renda2 / P_Preços[1, 0], 0], label='Orçamento competitivo', color='blue')  # Linha que conecta os limites
plt.xlabel('Quantidade do primeiro item')
plt.ylabel('Quantidade do segundo item')
plt.title('Gráfico do Orçamento Competitivo')
plt.legend()
plt.grid(True)
plt.show()


# Calculando o gradiente da matriz
#gradiente_x, gradiente_y = np.gradient(matriz)


# Definindo as variáveis
#x, y, L = sp.symbols('x y L')

# Definindo a expressão
#expr = 2*x**4 - L*(4*x + 5*y) - 3

# Calculando a derivada em relação a x
#derivada_x = sp.diff(expr, x)

# Calculando a derivada em relação a y
#derivada_y = sp.diff(expr, y)

#print("Derivada em relação a x:")
#print(derivada_x)

#print("\nDerivada em relação a y:")
#print(derivada_y)


# Definindo as variáveis e a função objetivo
#x, y, L = sp.symbols('x y L')
#f_obj = 2*x**4 - L*(4*x + 5*y) - 3

# Definindo as restrições de desigualdade e igualdade
#constraint1 = 4*x + 5*y - 10  # Exemplo de restrição de desigualdade
#constraint2 = 2*x - y - 1     # Exemplo de restrição de igualdade

# Calculando as derivadas parciais da função objetivo
#df_dx = sp.diff(f_obj, x)
#df_dy = sp.diff(f_obj, y)

# Resolvendo as condições de KKT
#kkt_conditions = [df_dx, df_dy, constraint1, constraint2]
#solution = sp.solve(kkt_conditions, (x, y, L))

#print("Solução encontrada:")
#print(solution)