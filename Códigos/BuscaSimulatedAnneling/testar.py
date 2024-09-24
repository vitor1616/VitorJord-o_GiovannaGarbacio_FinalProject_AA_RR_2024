import pandas as pd

def calcular_custos(rota_csv, arestas_csv, vertices_csv):
    arestas = pd.read_csv(arestas_csv)
    vertices = pd.read_csv(vertices_csv)
    rota = pd.read_csv(rota_csv)
    
    distancia_total = 0
    peso_total = 0

    for i in range(len(rota) - 1):
        no_atual = rota.iloc[i]['No']
        proximo_no = rota.iloc[i + 1]['No']
        aresta = arestas.loc[(arestas['Source'] == no_atual) & (arestas['Target'] == proximo_no)]
        if aresta.empty:
            aresta = arestas.loc[(arestas['Source'] == proximo_no) & (arestas['Target'] == no_atual)]
        if not aresta.empty:
            distancia_total += aresta['Distancia'].values[0]
        peso_total += vertices.loc[vertices['No'] == no_atual, 'Peso'].values[0]

    peso_total += vertices.loc[vertices['No'] == rota.iloc[-1]['No'], 'Peso'].values[0]

    alpha = 0.4
    custo_total = alpha * distancia_total - (1 - alpha) * peso_total

    return custo_total, distancia_total, peso_total


arestas_csv = 'ApenasParadas/grafo_paradas_somente_paradas_ARESTAS_COM_PESO.csv'
vertices_csv = 'ApenasParadas/grafo_paradas_somente_PARADAS.csv'

resultados = []


for i in range(1, 13):
    rota_csv = f'BuscaSimulatedAnneling/rota_simulated_annealing{i}.csv'
    custo_total, distancia_total, peso_total = calcular_custos(rota_csv, arestas_csv, vertices_csv)
    resultados.append((i, custo_total, distancia_total, peso_total))


with open('BuscaSimulatedAnneling/resultados_anneling.txt', 'w') as f:
    for i, custo, distancia, peso in resultados:
        f.write(f"Rota {i}: Custo total: {custo}, Distância total: {distancia}, Peso total: {peso}\n")

print("Resultados salvos em 'resultados_custos.txt'")
