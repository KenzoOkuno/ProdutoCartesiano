import tkinter as tk
# Importa a biblioteca Tkinter para criar interfaces gráficas (GUI)

from itertools import product
# Importa a função 'product' do módulo itertools
# Usada para calcular todas as combinações possíveis entre dois conjuntos (produto cartesiano)

# Função chamada quando o usuário clica no botão "Gerar Produto Cartesiano"
def gerar_produto():
    # Lê os valores digitados no Entry do conjunto A e separa por vírgula
    set_a = entry_a.get().split(',')
    
    # Lê os valores digitados no Entry do conjunto B e separa por vírgula
    set_b = entry_b.get().split(',')
    
    # Remove espaços extras e elementos vazios de A
    set_a = [x.strip() for x in set_a if x.strip()]
    
    # Remove espaços extras e elementos vazios de B
    set_b = [x.strip() for x in set_b if x.strip()]
    
    # Calcula o produto cartesiano: todos os pares (a, b) com a em A e b em B
    resultado = list(product(set_a, set_b))
    
    # Limpa a Listbox onde os resultados são mostrados, caso haja resultados anteriores
    resultado_box.delete(0, tk.END)
    
    # Para cada par do produto cartesiano, insere na Listbox
    for par in resultado:
        resultado_box.insert(tk.END, str(par))  # Converte o par para string antes de inserir
    
    # Atualiza a Label de informações mostrando o tamanho dos conjuntos e do produto
    info_label.config(text=f"|A| = {len(set_a)}, |B| = {len(set_b)}, |A×B| = {len(resultado)}")

# Cria a janela principal do programa
root = tk.Tk()

# Define o título da janela
root.title("Simulador de Produto Cartesiano")

# Label explicando onde digitar os elementos do conjunto A
tk.Label(root, text="Conjunto A (separe por vírgula):").grid(row=0, column=0, sticky='w')

# Entry para o usuário digitar os elementos do conjunto A
entry_a = tk.Entry(root, width=30)
entry_a.grid(row=0, column=1)  # Posiciona na linha 0, coluna 1

# Label explicando onde digitar os elementos do conjunto B
tk.Label(root, text="Conjunto B (separe por vírgula):").grid(row=1, column=0, sticky='w')

# Entry para o usuário digitar os elementos do conjunto B
entry_b = tk.Entry(root, width=30)
entry_b.grid(row=1, column=1)  # Posiciona na linha 1, coluna 1

# Botão que, ao ser clicado, chama a função gerar_produto()
tk.Button(root, text="Gerar Produto Cartesiano", command=gerar_produto).grid(row=2, column=0, columnspan=2, pady=10)

# Listbox que mostrará os pares do produto cartesiano
resultado_box = tk.Listbox(root, width=40)
resultado_box.grid(row=3, column=0, columnspan=2, pady=10)  # Ocupa duas colunas

# Label que mostrará informações como |A|, |B| e |A×B|
info_label = tk.Label(root, text="|A| = 0, |B| = 0, |A×B| = 0")
info_label.grid(row=4, column=0, columnspan=2)

# Inicia o loop principal da janela Tkinter, mantendo-a aberta e interativa
root.mainloop()