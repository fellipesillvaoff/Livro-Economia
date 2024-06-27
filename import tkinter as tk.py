import tkinter as tk
import pyperclip

# Função para copiar o texto para a área de transferência
def copiar_texto(texto):
    pyperclip.copy(texto)
    label.config(text=f"Copiado: {texto}")

# Função para inserir texto na posição atual do cursor na entrada
def inserir_texto(texto):
    cursor_pos = entrada.index(tk.INSERT)
    entrada.insert(cursor_pos, texto)

# Função para abrir a janela de fração
def abrir_janela_fracao():
    janela_fracao = tk.Toplevel(root)
    janela_fracao.title("Inserir Fração")
    janela_fracao.geometry("300x100")

    tk.Label(janela_fracao, text="Numerador:").grid(row=0, column=0, padx=5, pady=5)
    numerador_entry = tk.Entry(janela_fracao)
    numerador_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(janela_fracao, text="Denominador:").grid(row=1, column=0, padx=5, pady=5)
    denominador_entry = tk.Entry(janela_fracao)
    denominador_entry.grid(row=1, column=1, padx=5, pady=5)

    def inserir_fracao():
        numerador = numerador_entry.get()
        denominador = denominador_entry.get()
        fracao = f"({numerador}/{denominador})"
        inserir_texto(fracao)
        janela_fracao.destroy()

    tk.Button(janela_fracao, text="Inserir", command=inserir_fracao).grid(row=2, columnspan=2, pady=10)

# Criação da janela principal
root = tk.Tk()
root.title("Teclado Virtual de Símbolos")
root.geometry("300x400")

# Certifica que a janela fica sempre no topo
root.wm_attributes('-topmost', 1)

# Lista de símbolos
simbolos = [
    ("α", "Letra grega alfa"),
    ("β", "Letra grega beta"),
    ("γ", "Letra grega gama"),
    ("δ", "Letra grega delta"),
    ("Δ", "Letra grega Delta (maiúscula)"),
    ("ε", "Letra grega épsilon"),
    ("θ", "Letra grega teta"),
    ("λ", "Letra grega lambda"),
    ("μ", "Letra grega mu"),
    ("π", "Letra grega pi"),
    ("ρ", "Letra grega rho"),
    ("σ", "Letra grega sigma"),
    ("φ", "Letra grega fi"),
    ("ω", "Letra grega ômega"),
    ("ℯ", "Número de Euler"),
    ("∞", "Infinito"),
    ("∑", "Somatório"),
    ("∏", "Produtório"),
    ("√", "Raiz quadrada"),
    ("∫", "Integral"),
    ("≈", "Aproximadamente igual"),
    ("≠", "Diferente"),
    ("≤", "Menor ou igual"),
    ("≥", "Maior ou igual"),
    ("e^x", "Exponencial"),
    ("d/dx", "Derivada"),
    ("∂", "Derivada parcial"),
    ("sin", "Seno"),
    ("cos", "Cosseno"),
    ("tan", "Tangente"),
    ("θ", "Theta"),
    ("∠", "Ângulo"),
    ("∇", "Nabla (gradiente)"),
    ("⊥", "Perpendicular"),
    ("∥", "Paralelo"),
    ("≡", "Congruente"),
    ("ψ", "Letra grega psi")
]

# Label para exibir mensagens de confirmação
label = tk.Label(root, text="")
label.grid(row=0, column=0, columnspan=3, pady=10)

# Adicionando os botões para cada símbolo em uma grade de 3 colunas
for index, (simbolo, descricao) in enumerate(simbolos):
    row = (index // 3) + 1  # Ajusta a linha para deixar espaço para o label
    column = index % 3
    button = tk.Button(root, text=simbolo, width=8, command=lambda s=simbolo: inserir_texto(s))
    button.grid(row=row, column=column, padx=5, pady=5)

# Botão para abrir a janela de fração
botao_fracao = tk.Button(root, text="a/b", command=abrir_janela_fracao)
botao_fracao.grid(row=len(simbolos)//3 + 2, column=1, pady=10)

# Entrada de texto para a expressão
entrada = tk.Entry(root, width=20)
entrada.grid(row=len(simbolos)//3 + 2, column=0, padx=5)

# Executando o loop principal da interface
root.mainloop()
