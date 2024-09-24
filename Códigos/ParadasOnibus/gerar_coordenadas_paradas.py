from geopy.geocoders import Nominatim

# OBTER LATITUDE E LONGITUDE APARTIR DE ENDEREÇO
def get_lat_long(address):
    geolocator = Nominatim(user_agent="unique_application_name")
    try:
        location = geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except Exception as e:
        return f"Erro: {e}"

# LISTA DE TODOS OS ENDEREÇOS DE TODAS AS ROTAS
addresses = [
    "Rua Pedro Barbosa Da Silva, Boa Vista, Roraima",
    "Rua Estrela D'Álva, 1872, Boa Vista, Roraima",
    "R. Ametista, 631 - Jóquei Clube, Boa Vista, Roraima",
    "Escola Estadual Antônio Carlos Da Silva Natalino, Boa Vista, Roraima",
    "Rua José Francisco 745, Boa Vista, Roraima",
    "Rua Raimundo Penafort, 1549, Boa Vista, Roraima",
    "Escola Estadual Alcides Rodrigues Santos, Boa Vista, Roraima",
    "Rua Raimundo Penafort, 475, Boa Vista, Roraima",
    "Rua Raimundo Penafort, 177, Boa Vista, Roraima",
    "Via das Flores, 7042 - Pricumã, Boa Vista, Roraima",
    "Via Das Flores, 1959, Boa Vista, Roraima",
    "Via das Flores, 1614 - Pricumã, Boa Vista, Roraima",
    "Instituto Federal De Roraima - Campus Boa Vista, Boa Vista, Roraima",
    "Av. Glaycon de Paiva, 1778 - Mecejana, Boa Vista, Roraima",
    "Rua Pacaraima, Boa Vista, Roraima",
    "Posto Br, Boa Vista, Roraima",
    "Fórum Advogado Sobral Pinto, Boa Vista, Roraima",
    "Terminal Centro, Boa Vista, Roraima",
    "Rua Silo 153, Boa Vista, Roraima",
    "Parque Municipal Germano Augusto Sampaio, Boa Vista, Roraima",
    "Vila Olímpica, Boa Vista, Roraima",
    "Rua Pedro Aldemar Bantim, 991, Boa Vista, Roraima",
    "Rua Abdo Said Rezel, 115, Boa Vista, Roraima",
    "Rua Abdo Said Rezel, 410, Boa Vista, Roraima",
    "Rua Abdo Said Rezel, 782, Boa Vista, Roraima",
    "Rua José Renato Hadad, 258, Boa Vista, Roraima",
    "Rua Izidio Galdino Da Silva, 1300, Boa Vista, Roraima",
    "Rua Tertuliano Cardoso Ramos, 1450, Boa Vista, Roraima",
    "Rua Tertuliano Cardoso Ramos, 1674, Boa Vista, Roraima",
    "Rua Sólon Rodrigues Pessoa, Boa Vista, Roraima",
    "Av. Abel Monteiro Reis, Boa Vista, Roraima",
    "Rua Sólon Rodrigues Pessoa, 1353, Boa Vista, Roraima",
    "Rua Sólon Rodrigues Pessoa, 765, Boa Vista, Roraima",
    "Rua Sólon Rodrigues Pessoa, 571, Boa Vista, Roraima",
    "Rua Sólon Rodrigues Pessoa, 285, Boa Vista, Roraima",
    "Rua Doutor Rubem Lima Filho, 155, Boa Vista, Roraima",
    "Rua Doutor Rubem Lima Filho, 1, Boa Vista, Roraima",
    "R. Raimundo Penafort, 2331 - Asa Branca, Boa Vista, Roraima",
    "Praça Do Cambará, Boa Vista, Roraima",
    "R. Raimundo Penafort, 1549 - Asa Branca, Boa Vista, Roraima",
    "Escola Estadual Alcides Rodrigues Santos, Boa Vista, Roraima",
    "Rua Raimundo Penafort, 475, Boa Vista, Roraima",
    "Rua Raimundo Penafort, 177, Boa Vista, Roraima",
    "R. das Extremosas, 312 - Pricumã, Boa Vista, Roraima",
    "Via Das Flores, 1959, Boa Vista, Roraima",
    "Via das Flores, 1614 - Pricumã, Boa Vista - Roraima",
    "Instituto Federal De Roraima - Campus Boa Vista , Boa Vista, Roraima",
    "Av. Glaycon de Paiva, 1778 - Mecejana, Boa Vista, Roraima",
    "Rua Pacaraima B/C, Boa Vista, Roraima",
    "Teatro Municipal, Boa Vista, Roraima",
    "Av. Presidente Castelo Branco, 1899-1999, Boa Vista, Roraima",
    "Av. Nossa Senhora Da Consolata, 2281, Boa Vista, Roraima",
    "Terminal Centro, Boa Vista, Roraima",
    "Hospital Coronel Mota, Boa Vista, Roraima",
    "Rua Severino Soares De Freitas, 2670, Boa Vista, Roraima",
    "Rua Guariguara, 797, Boa Vista, Roraima",
    "Av. Ville Roy, 2670, Caçari, Boa Vista, Roraima",
    "Praça Do Mirandinha, Boa Vista, Roraima",
    "Av. Ville Roy, 3372, Boa Vista, Roraima",
    "Av. Ville Roy, 3642, Boa Vista, Roraima",
    "Avenida Ville Roy, 4213, Boa Vista, Roraima",
    "Av. Maj. Williams, 1018 - São Francisco, Boa Vista, Roraima",
    "Av. Ville Roy, 5492, Boa Vista, Roraima",
    "Terminal Centro, Boa Vista, Roraima",
    "Av. Cap. Ene Garcês - Centro, Boa Vista, Roraima",
    "Sesc Roraima, Boa Vista, Roraima",
    "Av. Mário Homem De Melo, 514, Boa Vista, Roraima",
    "Avenida Mário Homem De Melo, Boa Vista, Roraima",
    "Av. Mário Homem De Melo, 1182, Boa Vista, Roraima",
    "Av. Mário Homem De Melo, 1540, Boa Vista, Roraima",
    "Rua Brás De Aguiar, Boa Vista, Roraima",
    "Avenida Mário Homem De Melo, 2310, Boa Vista, Roraima",
    "Av. Mário Homem De Melo, 2814, Boa Vista, Roraima",
    "Av. Mário Homem De Melo, 3326, Boa Vista, Roraima",
    "Av. Mário Homem De Melo, 3604, Boa Vista, Roraima",
    "Av. Mário Homem De Melo, 3980, Boa Vista, Roraima",
    "Escola Estadual Vovó Julia, Boa Vista, Roraima",
    "Av. Nossa Senhora De Nazaré, Boa Vista, Roraima",
    "Praça Mané Garrincha, Boa Vista, Roraima",
    "Av. São Sebastião 1439, Boa Vista, Roraima",
    "Av. General Ataíde Teive, 5528, Boa Vista, Roraima",
    "Av. General Ataíde Teive, 6204, Boa Vista, Roraima",
    "Rua Betel, 701, Boa Vista, Roraima",
    "Rua Closvaldo Paes Carolino, Boa Vista, Roraima",
    "Rua Laura Pinheiro Maia, 1695, Boa Vista, Roraima",
    "Rua Laura Pinheiro Maia, 1299, Boa Vista, Roraima",
    "Rua Izidio Galdino Da Silva, 363, Boa Vista, Roraima",
    "Rua Izidio Galdino Da Silva, 712, Boa Vista, Roraima",
    "Rua Izidio Galdino Da Silva, 1016, Boa Vista, Roraima",
    "Rua Izidio Galdino Da Silva, 1300, Boa Vista, Roraima",
    "Rua Izidio Galdino Da Silva, 1962, Boa Vista, Roraima",
    "Rua Major Ecildon Pinto, S/N, Boa Vista, Roraima",
    "R. CC-15, 204 - Laura Moreira, Boa Vista, Roraima",
    "Rua N Nove, 2253, Boa Vista, Roraima",
    "R. Severino Soares de Freitas, 1685, Paraviana, Boa Vista, Roraima",
    "Avenida Amazonas 507, Boa Vista, Roraima",
    "Praça do Centro Cívico, 974, Centro, Boa Vista, Roraima",
    "Av. Capitão Júlio Bezerra, 2409, Boa Vista, Roraima",
    "Av. João Alencar, 2000, Boa Vista, Roraima",
    "Av. Capitão Júlio Bezerra, 1013, Boa Vista, Roraima",
    "Rua Barão Do Rio Branco, 150, Boa Vista, Roraima",
    "Av. Cap. Ene Garcês, 2731, Aeroporto, Boa Vista, Roraima",
    "Av. Cap. Ene Garcês, 02, Centro, Boa Vista, Roraima",
    "R. João Barbosa, 143, Mecejana, Boa Vista, Roraima",
    "Av. Mário Homem de Melo, 514, Centro, Boa Vista, Roraima",
    "Av. Mário Homem de Melo, 1183, Mecejana, Boa Vista, Roraima",
    "Av. Mário Homem De Melo, 1540, Boa Vista, Roraima",
    "Rua Brás De Aguiar, 200, Boa Vista, Roraima",
    "Av. Mário Homem de Melo, 2310, Mecejana, Boa Vista, Roraima",
    "Av. Mário Homem De Melo, 2814, Boa Vista, Roraima",
    "Av. Mário Homem De Melo, 3326, Boa Vista, Roraima",
    "Av. Mário Homem De Melo, 3604, Boa Vista, Roraima",
    "Av. Mário Homem De Melo, 3980, Boa Vista, Roraima",
    "Av. Mário Homem de Melo, 4665, Caimbé, Boa Vista, Roraima",
    "Av. Nossa Senhora De Nazaré, 1200, Boa Vista, Roraima",
    "Av. Mário Homem de Melo, 5692, Tancredo Neves, Boa Vista, Roraima",
    "Av. São Sebastião, 1439, Tancredo Neves, Boa Vista, Roraima",
    "Av. General Ataíde Teive, 5528, Boa Vista, Roraima",
    "Av. Gen. Ataíde Teive, 6204, Dr. Silvio Leite, Boa Vista, Roraima",
    "Rua Sião, 789, Boa Vista, Roraima",
    "Av. General Ataíde Teive, 6868, Boa Vista, Roraima",
    "Av. General Ataíde Teive, 7174, Boa Vista, Roraima",
    "Av. General Ataíde Teive, 7624, Boa Vista, Roraima",
    "Av. Dos Garimpeiros, 2345, Boa Vista, Roraima",
    "Av. General Ataíde Teive, 8998 , Boa Vista, Roraima",
    "Av. Santo Antônio, 1025, Boa Vista, Roraima",
    "Av. Equinócios, 800, Boa Vista, Roraima",
    "Rua Noroeste, 2347, Boa Vista, Roraima",
    "Rua Major Ecildon Pinto, 246, Boa Vista, Roraima",
    "Rua Severino Soares De Freitas, 2670, Boa Vista, Roraima",
    "Rua Guariguara, 797, Boa Vista, Roraima",
    "Av. Ville Roy, 1544, Caçari, Boa Vista, Roraima",
    "Av. Ville Roy, 19412, Boa Vista, Roraima",
    "Av. Ville Roy, 2869, Caçari, Boa Vista Roraima",
    "R. da Tangerineira, 440 Caçari, Boa Vista, Roraima",
    "Av. Ville Roy, 3372, Boa Vista, Roraima",
    "Av. Ville Roy, 3642, Boa Vista, Roraima",
    "Avenida Ville Roy, 4213, Boa Vista, Roraima",
    "Av. Santos Dumont, 760, São Pedro, Boa Vista, Roraima",
    "Av. Santos Dumont - São Pedro, Boa Vista, Roraima",
    "Av. Maj. Williams, 1018, São Francisco, Boa Vista, Roraima",
    "Av. Ville Roy, 5492, Boa Vista, Roraima",
    "Terminal Centro, Boa Vista, Roraima",
    "Av. Ville Roy, 7806, Boa Vista, Roraima",
    "Av. Ville Roy, 8336, Boa Vista, Roraima",
    "Rodoviária Internacional De Boa Vista, Boa Vista, Roraima",
    "Av. Brasil, 175, Pricumã, Boa Vista, Roraima",
    "Escola Estadual Carlos Casadio, Boa Vista, Roraima",
    "Av. Centenário, 1268, Boa Vista, Roraima",
    "Av. Roma, 319, Centenário, Boa Vista, Roraima",
    "R. Raio Solar, Jóquei Clube, Boa Vista, Roraima",
    "Rua Izidio Galdino Da Silva, 363, Boa Vista, Roraima",
    "Rua Izidio Galdino Da Silva, 712, Boa Vista, Roraima",
    "Rua Izidio Galdino Da Silva, 1016, Boa Vista, Roraima",
    "Rua Izidio Galdino Da Silva, 1300, Boa Vista, Roraima",
    "Rua Izidio Galdino Da Silva, 1962, Boa Vista, Roraima",
    "Rua Major Ecildon Pinto, S/N, Boa Vista, Roraima",
    "R. CC-15, 204, Laura Moreira, Boa Vista, Roraima",
    "Rua Major Ecildon Pinto, 246, Boa Vista, Roraima"
]


# LIMITES DE LATITUDE E LONGITUDE
min_lat = 2.796121002193689
max_lat = 2.8686450537844626
min_long = -60.75226652893248

# SALVAR OS DADOS EM ARQUIVO
with open("ParadasOnibus\coordenadas_paradas.txt", "w") as file:
    for address in addresses:
        coordinates = get_lat_long(address)
        if coordinates:
            lat, long = coordinates
            # Verificar se a parada está dentro dos limites especificados
            if lat > min_lat and lat < max_lat and long > min_long:
                file.write(f"{lat}, {long}, {address}\n")
                print(f"{lat}, {long}, {address}\n")
            else:
                print(f"Parada fora dos limites: {address}\n")
        else:
            file.write(f"Erro ao obter dados para o endereço: {address}\n")
            print(f"Erro ao obter dados para o endereço: {address}\n")