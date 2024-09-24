import networkx as nx
import osmnx as ox
import json
import csv

# CARREGAR GRAFO INICIAL
with open('Grafo_inicial\grafo_inicial_NOS.json', 'r') as f:
    data = json.load(f)
G = nx.node_link_graph(data)

def ler_paradas(arquivo_paradas):
    paradas = []
    with open(arquivo_paradas, 'r') as f:
        for linha in f:
            lat, lon, endereco = linha.strip().split(', ', 2)  # Separar lat, lon e endereço
            paradas.append((float(lat), float(lon), endereco))  
    return paradas

# CARREGAR COORDENADAS DAS PARADAS
paradas = ler_paradas('ParadasOnibus\coordenadas_paradas.txt')

# Definir uma distância máxima (em metros) para associar uma parada a um nó
distancia_maxima = 100 

# ASSOCIAR PARADAS A NÓS E DEFINIR PESO (qauntidade de associação ao mesmo vértice)
peso_nos = {}
for lat, lon, endereco in paradas:
    no_proximo = ox.distance.nearest_nodes(G, lon, lat)  
    lat_no_proximo = G.nodes[no_proximo]['y']
    lon_no_proximo = G.nodes[no_proximo]['x']

    distancia = ox.distance.great_circle(lat, lon, lat_no_proximo, lon_no_proximo)
    if distancia <= distancia_maxima:
        if no_proximo in peso_nos:
            peso_nos[no_proximo] += 1  
        else:
            peso_nos[no_proximo] = 1 
    else:
        print(f"Parada em {endereco} não associada a nenhum nó devido à distância ({distancia:.2f} metros).")

for no, peso in peso_nos.items():
    G.nodes[no]['peso'] = peso  

# SALVAR EM .csv
with open('GrafoParadas_V3/grafo_paradas_VERTICES.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['No', 'Latitude', 'Longitude', 'Peso'])  
    for no, dados in G.nodes(data=True):
        lat = dados.get('y', None)  # Latitude
        lon = dados.get('x', None)  # Longitude
        peso = dados.get('peso', 0)  # Peso associado ao nó (0 se não houver peso)
        writer.writerow([no, lat, lon, peso])
        
with open('GrafoParadas_V3/grafo_paradas_ARESTAS.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Source', 'Target', 'Distancia'])  # Cabeçalhos
    for u, v, data_edge in G.edges(data=True):
        distancia = data_edge.get('length', 0)  # Obter a distância (comprimento) da aresta
        writer.writerow([u, v, distancia])

data_com_pesos = nx.node_link_data(G)
with open('GrafoParadas_V3/grafo_paradas.json', 'w') as f:
    json.dump(data_com_pesos, f, indent=4) 

print("Nós e arestas exportados para CSV e grafo atualizado salvo em JSON!")
