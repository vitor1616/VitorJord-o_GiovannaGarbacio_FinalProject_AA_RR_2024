import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# LER GRAFO
def ler_nos_csv(arquivo_csv):
    df = pd.read_csv(arquivo_csv)
    G = nx.Graph()
    for _, linha in df.iterrows():
        no = int(linha['No'])
        lat = float(linha['Latitude'])
        lon = float(linha['Longitude'])
        peso = linha['Peso']
        G.add_node(no, x=lon, y=lat, peso=peso) 
    return G

def ler_arestas_csv(arquivo_csv, G):
    df = pd.read_csv(arquivo_csv)
    for _, linha in df.iterrows():
        source = int(linha['Source'])
        target = int(linha['Target'])
        distancia = float(linha['Distancia'])
        G.add_edge(source, target, length=distancia) 
    return G

G = ler_nos_csv('GrafoParadas_V3\grafo_paradas_VERTICES.csv')
G = ler_arestas_csv('GrafoParadas_V3\grafo_paradas_ARESTAS.csv', G)


pos = {n: (G.nodes[n]['x'], G.nodes[n]['y']) for n in G.nodes()}  # Posicionar os nós
pesos = nx.get_node_attributes(G, 'peso')  # Obter pesos dos nós
nodos_com_peso = {n: peso for n, peso in pesos.items() if peso > 0}
nodos_sem_peso = [n for n in G.nodes if n not in nodos_com_peso]

cmap = plt.get_cmap('cool')  
norm = plt.Normalize(vmin=0, vmax=max(pesos.values(), default=1)) 
node_colors = [cmap(norm(pesos[n])) if n in nodos_com_peso else 'lightgray' for n in G.nodes()]
node_sizes = [70 if n in nodos_com_peso else 5 for n in G.nodes()]  # Aumentar o tamanho dos nós com peso

# PLOT DO GRAFO
fig, ax = plt.subplots(figsize=(12, 10))  # Criar figura e eixo
nx.draw(G, pos, with_labels=False, node_size=node_sizes, node_color=node_colors, edge_color='gray', alpha=0.5, ax=ax)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([]) 
cbar = plt.colorbar(sm, ax=ax, label='Peso dos Nós')

plt.title('Grafo de Boa Vista com Pesos das Paradas')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# SALVAR FIGURA
plt.savefig('GrafoParadas_V3/grafo_paradas.png', format='png', bbox_inches='tight')
plt.show()
