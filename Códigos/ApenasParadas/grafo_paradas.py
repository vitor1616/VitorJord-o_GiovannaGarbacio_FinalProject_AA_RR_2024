import pandas as pd
import networkx as nx
from itertools import combinations

vertices_df = pd.read_csv('GrafoParadas_V3/grafo_paradas_VERTICES.csv')
arestas_df = pd.read_csv('GrafoParadas_V3/grafo_paradas_ARESTAS.csv')
G_completo = nx.Graph()

print("Adicionando vértices ao grafo completo...")
for _, row in vertices_df.iterrows():
    G_completo.add_node(row['No'], pos=(row['Latitude'], row['Longitude']), peso=row['Peso'])

print("Adicionando arestas ao grafo completo...")
for _, row in arestas_df.iterrows():
    G_completo.add_edge(row['Source'], row['Target'], distancia=row['Distancia'])

print("Filtrando vértices que representam paradas de ônibus...")
paradas_onibus = vertices_df[vertices_df['Peso'] > 0]
print(f"Total de paradas de ônibus encontradas: {len(paradas_onibus)}")
G_paradas = nx.Graph()
print("Adicionando paradas de ônibus ao novo grafo...")
for _, row in paradas_onibus.iterrows():
    G_paradas.add_node(row['No'], pos=(row['Latitude'], row['Longitude']), peso=row['Peso'])


print("Calculando a menor distância entre cada par de paradas de ônibus...")
for (no1, dados1), (no2, dados2) in combinations(G_paradas.nodes(data=True), 2):
    try:
        # Calcular a menor distância usando o grafo completo
        menor_distancia = nx.shortest_path_length(G_completo, source=no1, target=no2, weight='distancia')
        G_paradas.add_edge(no1, no2, distancia=menor_distancia)
        print(f"Caminho entre {no1} e {no2} achado.")
    except nx.NetworkXNoPath:
        print(f"Sem caminho entre parada {no1} e parada {no2}")

print(f"Total de arestas no novo grafo de paradas: {G_paradas.number_of_edges()}")

print("Visualizando algumas estatísticas do grafo de paradas de ônibus...")
print(f"Número de nós: {G_paradas.number_of_nodes()}")
print(f"Número de arestas: {G_paradas.number_of_edges()}")

arestas_com_peso = []

for u, v, data_edge in G_paradas.edges(data=True):
    peso_u = G_paradas.nodes[u]['peso']
    peso_v = G_paradas.nodes[v]['peso']
    distancia = data_edge.get('distancia', 0)
    arestas_com_peso.append({
        'Source': u,
        'Target': v,
        'Distancia': distancia,
        'Peso_Source': peso_u,
        'Peso_Target': peso_v
    })

arestas_com_peso_df = pd.DataFrame(arestas_com_peso)
arestas_com_peso_df.to_csv('ApenasParadas/grafo_paradas_somente_paradas_ARESTAS_COM_PESO.csv', index=False)

print("Salvando os vértices das paradas de ônibus em um arquivo CSV...")
vertices_paradas = []

for node in G_paradas.nodes(data=True):
    vertices_paradas.append({
        'No': node[0],
        'Latitude': node[1]['pos'][0],
        'Longitude': node[1]['pos'][1],
        'Peso': node[1]['peso']
    })

vertices_paradas_df = pd.DataFrame(vertices_paradas)
vertices_paradas_df.to_csv('ApenasParadas/grafo_paradas_somente_PARADAS.csv', index=False)

print("Processamento concluído. Novos arquivos salvos em 'grafo_paradas_somente_paradas_ARESTAS_COM_PESO.csv' e 'grafo_paradas_somente_PARADAS.csv'.")
