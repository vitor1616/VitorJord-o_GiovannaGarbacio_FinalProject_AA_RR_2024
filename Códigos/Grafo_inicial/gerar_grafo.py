import networkx as nx
import matplotlib.pyplot as plt
import osmnx as ox
import json
from shapely.geometry import LineString, Point

# CRIAÇÃO DO GRAFO DAS RUAS DE BOA VISTA
# 8000m em volta de Av. Cap. Ene Garcês - Centro (próximo à bola do centro)
raio = 8000
G = ox.graph_from_point((2.8232, -60.6753), dist=raio, network_type='drive')

# LIMITES PARA CORTE DO GRAFO
# Limites superior e inferior
latitude_min = 2.791287850298831
latitude_max = 2.868807440536532
# Área depois da Ponte dos  Macuxis
triangulo_pts = [
    (2.796345841907548, -60.67295339721996),
    (2.754938256631938, -60.609696179813106),
    (2.825407436933403, -60.600941449588426)
]
# Área depois da ponte do Cauamá
quadrado_pts = {
    'lat_min': 2.8404263518484227,
    'lat_max': 2.8651149554500437,
    'lon_min': -60.75869522588732,
    'lon_max': -60.68925819891027
}

# VERIFICAR SE UM PONTO ESTÁ AS ÁREAS DE CORTE
def estaDepoisCauame(lat, lon):
    return (quadrado_pts['lat_min'] <= lat <= quadrado_pts['lat_max'] and
            quadrado_pts['lon_min'] <= lon <= quadrado_pts['lon_max'])
def is_same_side(p1, p2, a, b):
    cross_product_1 = (b[0] - a[0]) * (p1[1] - a[1]) - (b[1] - a[1]) * (p1[0] - a[0])
    cross_product_2 = (b[0] - a[0]) * (p2[1] - a[1]) - (b[1] - a[1]) * (p2[0] - a[0])
    return cross_product_1 * cross_product_2 >= 0
def estaDepoisMacuxis(p, triangle):
    a, b, c = triangle
    return (is_same_side(p, a, b, c) and
            is_same_side(p, b, a, c) and
            is_same_side(p, c, a, b))
def verificarRemocao(node_data):
    lat, lon = node_data['y'], node_data['x']
    if lat < latitude_min or lat > latitude_max:
        return True
    point = (lat, lon)
    if estaDepoisMacuxis(point, triangulo_pts) or estaDepoisCauame(lat, lon):
        return True
    return False

nodes_to_remove = [node for node, data in G.nodes(data=True) if verificarRemocao(data)]
G.remove_nodes_from(nodes_to_remove)

# PLOT DA IMAGEM
fig, ax = ox.plot_graph(G, show=False)
plt.savefig('GrafoBV_V3/grafo_inicial.png', format='png', bbox_inches='tight')
plt.close(fig)  

# SALVAR EM .json
def geometry_to_coordinates(geometry):
    if isinstance(geometry, LineString):
        return list(geometry.coords)
    return geometry

data = nx.node_link_data(G)

for edge in data['links']:
    if 'geometry' in edge:
        edge['geometry'] = geometry_to_coordinates(edge['geometry'])

with open('GrafoBV_V3/grafo_inicial_NOS.json', 'w') as f:
    json.dump(data, f, indent=4)

arestas_com_distancias = {
    "directed": G.is_directed(),
    "multigraph": G.is_multigraph(),
    "graph": {},
    "nodes": [{"id": node} for node in G.nodes],
    "links": []
}

for u, v, data_edge in G.edges(data=True):
    distancia = data_edge.get('length', 0)  # 'length' armazena a distância em metros
    arestas_com_distancias["links"].append({
        'source': u,
        'target': v,
        'distancia': distancia
    })

with open('GrafoBV_V3/grafo_inical_ARESTAS.json', 'w') as f:
    json.dump(arestas_com_distancias, f, indent=4)

print("Exportações completas: grafo completo e arestas com distâncias.")
