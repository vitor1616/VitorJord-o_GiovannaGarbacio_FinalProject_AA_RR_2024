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

# Função para plotar o grafo com a rota
def plotar_rota_completa(G, rota, pos):
    pesos = nx.get_node_attributes(G, 'peso')
    cmap = plt.get_cmap('cool')
    norm = plt.Normalize(vmin=0, vmax=max(pesos.values(), default=1))
    node_colors = [cmap(norm(pesos[n])) if n in pesos else 'lightgray' for n in G.nodes()]
    node_sizes = [70 if n in pesos and pesos[n] > 0 else 1 for n in G.nodes()]

    fig, ax = plt.subplots(figsize=(12, 10))
    nx.draw(G, pos, with_labels=False, node_size=node_sizes, node_color=node_colors, edge_color='gray', alpha=0.5, ax=ax)

    for i in range(len(rota) - 1):
        no_atual = rota[i]
        proximo_no = rota[i + 1]
        try:
            caminho_curto = nx.shortest_path(G, source=no_atual, target=proximo_no, weight='length')
            caminho_arestas = list(zip(caminho_curto[:-1], caminho_curto[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=caminho_arestas, edge_color='red', width=2, ax=ax)
        except nx.NetworkXNoPath:
            print(f"Sem caminho entre {no_atual} e {proximo_no}")

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, label='Peso dos Nós')

    plt.title('Grafo de Boa Vista com Rota Simulated Annealing')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    plt.savefig('BuscaSimulatedAnneling\grafo_rota_simulated_annealing13.png', format='png', bbox_inches='tight')
    plt.show()

G = ler_nos_csv('GrafoParadas_V3/grafo_paradas_VERTICES.csv')
G = ler_arestas_csv('GrafoParadas_V3/grafo_paradas_ARESTAS.csv', G)

rota_df = pd.read_csv('BuscaSimulatedAnneling/rota_simulated_annealing13.csv')
rota = rota_df['No'].tolist()

pos = {n: (G.nodes[n]['x'], G.nodes[n]['y']) for n in G.nodes()} 

plotar_rota_completa(G, rota, pos)
