import pandas as pd
import numpy as np
import random
import math

def funcao_custo(rota, arestas, vertices, alpha=0.4):
    distancia_total = 0
    peso_total = 0

    for i in range(len(rota) - 1):
        no_atual = rota[i]
        proximo_no = rota[i + 1]
        aresta = arestas.loc[(arestas['Source'] == no_atual) & (arestas['Target'] == proximo_no)]
        if aresta.empty:
            aresta = arestas.loc[(arestas['Source'] == proximo_no) & (arestas['Target'] == no_atual)]
        if not aresta.empty:
            distancia_total += aresta['Distancia'].values[0]
        else:
            distancia_total += 10000

        peso_total += vertices.loc[vertices['No'] == no_atual, 'Peso'].values[0]

    peso_total += vertices.loc[vertices['No'] == rota[-1], 'Peso'].values[0]
    
    # FUNÇÃO DE CUSTO
    custo = alpha * distancia_total - (1 - alpha) * peso_total
    return custo

def gerar_vizinho(rota):
    nova_rota = rota.copy()
    i, j = random.sample(range(1, len(nova_rota) - 1), 2) 
    nova_rota[i], nova_rota[j] = nova_rota[j], nova_rota[i]
    return nova_rota

def simulated_annealing(arestas, vertices, origem, destino, temperatura_inicial=1000, resfriamento=0.980, iteracoes=2000):
    rota_inicial = [origem] + random.sample(list(vertices['No']), 10) + [destino, origem]  # Retornar à origem
    custo_atual = funcao_custo(rota_inicial, arestas, vertices)

    melhor_rota = rota_inicial
    melhor_custo = custo_atual
    temperatura = temperatura_inicial

    for i in range(iteracoes):
        nova_rota = gerar_vizinho(melhor_rota)
        novo_custo = funcao_custo(nova_rota, arestas, vertices)

        if novo_custo < custo_atual or random.uniform(0, 1) < math.exp((custo_atual - novo_custo) / temperatura):
            melhor_rota = nova_rota
            custo_atual = novo_custo

            if novo_custo < melhor_custo:
                melhor_rota = nova_rota
                melhor_custo = novo_custo

        temperatura *= resfriamento

    return melhor_rota, melhor_custo


vertices = pd.read_csv('ApenasParadas/grafo_paradas_somente_PARADAS.csv')
arestas = pd.read_csv('ApenasParadas/grafo_paradas_somente_paradas_ARESTAS_COM_PESO.csv')

origem = 1722357030.0  # Nó mais próximo de Parque Municipal Germano Augusto Sampaio
destino = 1710134592.0  # Nó mais próximo de Bosque dos Papagaios

melhor_rota, melhor_custo = simulated_annealing(arestas, vertices, origem, destino)

# Salvar a rota e o custo em um arquivo CSV
rota_df = pd.DataFrame({'No': melhor_rota})
rota_df.to_csv('ApenasParadas/rota_simulated_annealing13.csv', index=False)

print(f"Melhor rota encontrada: {melhor_rota}")
print(f"Custo da melhor rota: {melhor_custo}")
